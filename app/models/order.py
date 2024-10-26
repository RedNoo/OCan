from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime,ForeignKey
from app.models import User 

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str] = mapped_column(default="pending")
    total_amount: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[DateTime]

    user: Mapped["User"] = relationship("User", back_populates="orders")
