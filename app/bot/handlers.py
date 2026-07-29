from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler, filters

from telegram import ReplyKeyboardMarkup

from app.db.session import SessionLocal
from app.models.category import Category

from app.models.product import Product

from app.bot.keyboards import main_keyboard


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

        return products

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

    elif text == "⬅️ Menú principal":

        await update.message.reply_text(
            "Menú principal:",
            reply_markup=main_keyboard()
        )

    elif text == "🛒 Mi carrito":

        await update.message.reply_text(
            "Tu carrito está vacío."
        )

    elif text == "📦 Mis pedidos":

        await update.message.reply_text(
            "Todavía no tienes pedidos."
        )

    else:

        products = get_products_by_category(text)

        if products is not None:

            if len(products) == 0:

                await update.message.reply_text(
                    "Esta categoría no tiene productos."
                )

            else:

                message = f"🍗 {text}\n\n"

                for product in products:

                    message += (
                        f"• {product.name}\n"
                        f"💲 Precio: Bs. {product.price}\n\n"
                    )

                await update.message.reply_text(message)

        else:

            await update.message.reply_text(
                "Selecciona una opción del menú."
            )