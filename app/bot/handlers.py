from telegram import Update
from telegram.ext import ContextTypes

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