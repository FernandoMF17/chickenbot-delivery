from telegram.ext import (
    Application,
    CommandHandler,
)

from app.core.config import settings
from app.bot.handlers import start


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

    return application