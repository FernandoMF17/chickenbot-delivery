from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    status = Column(String(30), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    delivery_latitude = Column(Float, nullable=True)
    delivery_longitude = Column(Float, nullable=True)

    user = relationship("User", back_populates="orders")

    details = relationship("OrderDetail", back_populates="order")

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=True
    )
