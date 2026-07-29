from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    description = Column(String(255))

    price = Column(Float, nullable=False)

    stock = Column(Integer, default=0)

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )

    category = relationship(
        "Category",
        back_populates="products"
    )
    
    details = relationship(
    "OrderDetail",
    back_populates="product"
)