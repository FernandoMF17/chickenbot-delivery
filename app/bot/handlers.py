from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler, filters

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

async def menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    if text == "🍗 Ver categorías":

        await update.message.reply_text(
            "Mostrando categorías..."
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

        await update.message.reply_text(
            "Selecciona una opción del menú."
        )

