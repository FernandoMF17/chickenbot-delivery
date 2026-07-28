from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)

    quantity = Column(Integer, nullable=False)

    subtotal = Column(Float, nullable=False)

    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    order = relationship("Order", back_populates="details")

    product = relationship("Product", back_populates="details")