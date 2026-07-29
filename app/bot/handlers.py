from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler, filters

from telegram import ReplyKeyboardMarkup

from app.db.session import SessionLocal
from app.models.category import Category

from app.models.product import Product
from app.bot.keyboards import cart_keyboard
from app.models.user import User
from app.models.order import Order
from app.models.order_detail import OrderDetail

from app.bot.keyboards import (
    main_keyboard,
    products_keyboard,
)



async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    user = update.effective_user

    await update.message.reply_text(
        f"""
🍗 ¡Bienvenido a ChickenBot Delivery!

Hola {user.first_name}.

Desde este bot podrás:

• Ver nuestro catálogo.
• Agregar productos al carrito.
• Realizar pedidos.
• Consultar el estado de tus pedidos.

Selecciona una opción del menú 👇
""",
        reply_markup=main_keyboard()
    )

def categories_keyboard():

    db = SessionLocal()

    try:

        categories = (
            db.query(Category)
            .order_by(Category.name)
            .all()
        )

    finally:
        db.close()

    keyboard = []

    for category in categories:
        keyboard.append([category.name])

    keyboard.append(["⬅️ Menú principal"])

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

def get_products_by_category(category_name: str):

    db = SessionLocal()

    try:

        category = (
            db.query(Category)
            .filter(Category.name == category_name)
            .first()
        )

        if category is None:
            return None

        products = (
            db.query(Product)
            .filter(Product.category_id == category.id)
            .order_by(Product.name)
            .all()
        )

        return category, products

    finally:
        db.close()

def get_product_by_name(product_name: str):

    db = SessionLocal()

    try:

        product = (
            db.query(Product)
            .filter(Product.name == product_name)
            .first()
        )

        return product

    finally:
        db.close()

def get_or_create_user(update):

    db = SessionLocal()

    try:

        telegram_user = update.effective_user

        username = telegram_user.username

        if username is None:
            username = f"user_{telegram_user.id}"

        user = (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

        if user is None:

            user = User(
                username=username,
                full_name=telegram_user.full_name
            )

            db.add(user)
            db.commit()
            db.refresh(user)

        return user

    finally:
        db.close()

async def menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    if text == "🍗 Ver categorías":

        await update.message.reply_text(
            "Selecciona una categoría:",
            reply_markup=categories_keyboard()
        )

    elif text == "⬅️ Categorías":

        await update.message.reply_text(
            "Selecciona una categoría:",
            reply_markup=categories_keyboard()
        )

    elif text == "⬅️ Menú principal":

        await update.message.reply_text(
            "Menú principal:",
            reply_markup=main_keyboard()
        )

    elif text == "🛒 Mi carrito":

        cart = context.user_data.get("cart", {})

        if not cart:

            await update.message.reply_text(
                "🛒 Tu carrito está vacío."
            )

        else:

            message = "🛒 Tu carrito\n\n"

            total = 0

            for item in cart.values():

                subtotal = item["price"] * item["quantity"]

                total += subtotal

                message += (
                    f"• {item['name']}\n"
                    f"Cantidad: {item['quantity']}\n"
                    f"Subtotal: Bs. {subtotal}\n\n"
                )

            message += f"💰 Total: Bs. {total}"

            await update.message.reply_text(
                message,
                reply_markup=cart_keyboard()
            )

    elif text == "📦 Mis pedidos":

        await update.message.reply_text(
            "Todavía no tienes pedidos."
        )

    elif text == "🗑 Vaciar carrito":

        context.user_data["cart"] = {}

        await update.message.reply_text(
            "🗑 Carrito vaciado correctamente."
        )


    elif text.startswith("➕ "):

        product_name = text.replace("➕ ", "")

        product = get_product_by_name(product_name)

        if product is None:

            await update.message.reply_text(
                "Producto no encontrado."
            )
        elif product.stock <= 0:

            await update.message.reply_text(
                f"❌ {product.name} está agotado."
            )

            return

        else:

            cart = context.user_data.setdefault("cart", {})

            current_quantity = cart.get(product.id, {}).get("quantity", 0)

            if current_quantity >= product.stock:

                await update.message.reply_text(
                    f"❌ Solo quedan {product.stock} unidades disponibles de {product.name}."
                )

            else:

                if product.id in cart:

                    cart[product.id]["quantity"] += 1

                else:

                    cart[product.id] = {
                        "name": product.name,
                        "price": product.price,
                        "quantity": 1
                    }

                await update.message.reply_text(
                    f"✅ {product.name} agregado al carrito."
                )

    elif text == "✅ Confirmar pedido":

        cart = context.user_data.get("cart", {})

        if not cart:

            await update.message.reply_text(
                "🛒 Tu carrito está vacío."
            )

        else:

            user = get_or_create_user(update)

            db = SessionLocal()

            try:

                # Verificar stock antes de registrar el pedido
                for product_id, item in cart.items():

                    product = db.get(Product, product_id)

                    if product is None:

                        await update.message.reply_text(
                            "❌ Uno de los productos ya no existe."
                        )

                        return

                    if product.stock < item["quantity"]:

                        await update.message.reply_text(
                            f"❌ Stock insuficiente para {product.name}.\n"
                            f"Disponible: {product.stock}"
                        )

                        return

                # Crear pedido
                order = Order(
                    status="Pendiente",
                    user_id=user.id
                )

                db.add(order)
                db.flush()   # Obtiene el ID sin hacer commit

                # Crear detalles y descontar stock
                for product_id, item in cart.items():

                    product = db.get(Product, product_id)

                    product.stock -= item["quantity"]

                    detail = OrderDetail(
                        quantity=item["quantity"],
                        subtotal=item["price"] * item["quantity"],
                        order_id=order.id,
                        product_id=product_id
                    )

                    db.add(detail)

                db.commit()

                context.user_data["cart"] = {}

                await update.message.reply_text(
                    f"🎉 Pedido confirmado.\n\n"
                    f"Número de pedido: #{order.id}\n"
                    f"Estado: {order.status}",
                    reply_markup=main_keyboard()
                )

            except Exception:

                db.rollback()

                await update.message.reply_text(
                    "❌ Ocurrió un error al registrar el pedido."
                )

            finally:

                db.close()

    else:

        result = get_products_by_category(text)

        if result is not None:

            category, products = result

            if len(products) == 0:

                await update.message.reply_text(
                    "Esta categoría no tiene productos."
                )

            else:

                message = f"🍗 {category.name}\n\n"

                for product in products:

                    message += (
                        f"• {product.name}\n"
                        f"💲 Precio: Bs. {product.price}\n"
                        f"📦 Stock: {product.stock}\n\n"
                    )

                await update.message.reply_text(
                    message,
                    reply_markup=products_keyboard(category.id)
                )

        else:

            await update.message.reply_text(
                "Selecciona una opción del menú."
            )