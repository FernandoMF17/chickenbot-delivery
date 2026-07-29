from sqlalchemy import text
from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler, filters

from telegram import ReplyKeyboardMarkup

from app.db.session import SessionLocal
from app.models.category import Category
from app.models.delivery import Delivery
from app.models.product import Product
from app.bot.keyboards import cart_keyboard
from app.models.user import User
from app.models.order import Order
from app.models.order_detail import OrderDetail
from sqlalchemy.orm import joinedload

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

def get_user_orders(update):

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
            return []

        orders = (
            db.query(Order)
            .options(
                joinedload(Order.details).joinedload(OrderDetail.product)
            )
            .filter(Order.user_id == user.id)
            .order_by(Order.created_at.desc())
            .all()
        )

        return orders

    finally:
        db.close()

def get_delivery(access_code: str):

    db = SessionLocal()

    try:

        delivery = (
            db.query(Delivery)
            .filter(
                Delivery.access_code == access_code,
                Delivery.is_active == True
            )
            .first()
        )

        return delivery

    finally:
        db.close()

def update_order_location(
    order_id: int,
    latitude: float,
    longitude: float
):

    db = SessionLocal()

    try:

        order = db.get(Order, order_id)

        if order is None:
            return False

        order.delivery_latitude = latitude
        order.delivery_longitude = longitude

        db.commit()

        return True

    finally:
        db.close()

def get_pending_orders():

    db = SessionLocal()

    try:

        orders = (
            db.query(Order)
            .options(
                joinedload(Order.user),
                joinedload(Order.details).joinedload(OrderDetail.product)
            )
            .filter(Order.status == "Pendiente")
            .order_by(Order.created_at.asc())
            .all()
        )

        return orders

    finally:
        db.close()

async def delivery_login(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if len(context.args) != 1:

        await update.message.reply_text(
            "Uso:\n/delivery TU_CODIGO"
        )

        return

    access_code = context.args[0]

    delivery = get_delivery(access_code)

    if delivery is None:

        await update.message.reply_text(
            "❌ Código incorrecto."
        )

        return

    context.user_data["delivery_id"] = delivery.id

    await update.message.reply_text(
        f"✅ Bienvenido {delivery.full_name}.\n\n"
        "Autenticación correcta."
    )

async def pending_orders(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # Verificar autenticación
    if "delivery_id" not in context.user_data:

        await update.message.reply_text(
            "❌ Debes autenticarte primero.\n\n"
            "Usa:\n"
            "/delivery TU_CODIGO"
        )

        return

    # 👇 PASO 3 VA AQUÍ
    orders = get_pending_orders()

    if len(orders) == 0:

        await update.message.reply_text(
            "📦 No existen pedidos pendientes."
        )

        return

    # PASO 4
    message = "🚚 Pedidos pendientes\n\n"

    for order in orders:

        message += (
            f"🧾 Pedido #{order.id}\n"
            f"👤 Cliente: {order.user.full_name}\n"
            f"📌 Estado: {order.status}\n"
        )

        if (
            order.delivery_latitude is not None
            and
            order.delivery_longitude is not None
        ):

            maps = (
                "https://www.google.com/maps?q="
                f"{order.delivery_latitude},"
                f"{order.delivery_longitude}"
            )

            message += (
                f"📍 Ubicación:\n{maps}\n"
            )

        else:

            message += (
                "📍 Ubicación no registrada.\n"
            )

        message += "\n🍗 Productos:\n"

        for detail in order.details:

            message += (
                f"• {detail.product.name} x{detail.quantity}\n"
            )

        message += "\n"

    await update.message.reply_text(message)

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

        orders = get_user_orders(update)

        if len(orders) == 0:

            await update.message.reply_text(
                "📦 Todavía no tienes pedidos."
            )

        else:

            message = "📦 Historial de pedidos\n\n"

            for order in orders:

                fecha = order.created_at.strftime("%d/%m/%Y %H:%M")

                total = sum(
                    detail.subtotal
                    for detail in order.details
                )

                message += (
                    f"🧾 Pedido #{order.id}\n"
                    f"📅 Fecha: {fecha}\n"
                    f"📌 Estado: {order.status}\n\n"
                )

                message += "Productos:\n"

                for detail in order.details:

                    message += (
                        f"• {detail.product.name} x{detail.quantity}\n"
                    )

                message += (
                    f"\n💰 Total: Bs. {total}\n"
                    f"{'─' * 25}\n\n"
                )

            await update.message.reply_text(message)

    elif text == "🗑 Vaciar carrito":

        context.user_data["cart"] = {}

        await update.message.reply_text(
            "🗑 Carrito vaciado correctamente.",
            reply_markup=main_keyboard()
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
                context.user_data["pending_order_id"] = order.id
                context.user_data["waiting_location"] = True

                await update.message.reply_text(
                    f"🎉 Pedido #{order.id} registrado correctamente.\n\n"
                    "📍 Ahora comparte tu ubicación para la entrega."
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

async def receive_location(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not context.user_data.get("waiting_location"):
        return

    location = update.message.location

    order_id = context.user_data.get("pending_order_id")

    success = update_order_location(
        order_id,
        location.latitude,
        location.longitude
    )

    if not success:

        await update.message.reply_text(
            "❌ No se pudo registrar la ubicación."
        )

        return

    context.user_data.pop("waiting_location", None)
    context.user_data.pop("pending_order_id", None)

    await update.message.reply_text(
        "✅ Ubicación registrada correctamente."
    )