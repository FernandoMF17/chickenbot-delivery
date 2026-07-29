from sqlalchemy import Column, Integer, String, Boolean

from app.db.base import Base


class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    telegram_username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    access_code = Column(
        String(20),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )