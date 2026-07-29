from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from app.core.config import settings
from app.bot.handlers import (
    start,
    menu,
    delivery_login,
)

def create_bot():

    application = (
        Application.builder()
        .token(settings.BOT_TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    application.add_handler(
        CommandHandler(
            "delivery",
            delivery_login
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            menu
        )
    )

    return application