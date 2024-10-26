from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime, ForeignKey


class Cart(Base):
    __tablename__ = "carts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    total_amount: Mapped[float] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="cart")
    cart_items: Mapped[list["CartItem"]] = relationship(
        "CartItem", back_populates="cart"
    )
