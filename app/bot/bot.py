from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from app.core.config import settings

from app.bot.handlers import (
    start,
    menu,
    delivery_login,
    receive_location,
    pending_orders,
    start_delivery,
    finish_delivery,
    receive_delivery_photo,
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
            filters.LOCATION,
            receive_location
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            menu
        )
    )
    application.add_handler(
    CommandHandler(
        "pending",
        pending_orders
        )
    )
    
    application.add_handler(
    CallbackQueryHandler(
        start_delivery,
        pattern="^start_delivery:"
    )
)

    application.add_handler(
        CallbackQueryHandler(
            finish_delivery,
            pattern="^finish_delivery:"
        )
    )

    application.add_handler(
        MessageHandler(
            filters.PHOTO,
            receive_delivery_photo
        )
    )   

    return application