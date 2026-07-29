from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler, filters

from telegram import ReplyKeyboardMarkup

from app.db.session import SessionLocal
from app.models.category import Category

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
    elif text in [
        "Combos",
        "Bebidas",
        "Postres"
    ]:

        await update.message.reply_text(
            f"Mostrando productos de {text}..."
        )

    else:

        await update.message.reply_text(
            "Selecciona una opción del menú."
        )

