from telegram import ReplyKeyboardMarkup

from app.db.session import SessionLocal
from app.models.product import Product

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

def products_keyboard(category_id: int):

    db = SessionLocal()

    try:

        products = (
            db.query(Product)
            .filter(Product.category_id == category_id)
            .order_by(Product.name)
            .all()
        )

    finally:
        db.close()

    keyboard = []

    for product in products:
        keyboard.append([f"➕ {product.name}"])

    keyboard.append(["🛒 Mi carrito"])
    keyboard.append(["🗑 Vaciar carrito"])
    keyboard.append(["⬅️ Categorías"])

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

def cart_keyboard():

    keyboard = [
        ["✅ Confirmar pedido"],
        ["🗑 Vaciar carrito"],
        ["⬅️ Categorías"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )