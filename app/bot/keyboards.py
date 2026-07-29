from telegram import ReplyKeyboardMarkup


def main_keyboard():

    keyboard = [
        ["🍗 Ver categorías"],
        ["🛒 Mi carrito"],
        ["📦 Mis pedidos"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )