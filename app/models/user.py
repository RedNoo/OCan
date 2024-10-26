from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime
from app.models import Order, Cart

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created_at : Mapped[datetime]  = mapped_column(DateTime(timezone=True),default=datetime.now()) 

    orders: Mapped[list['Order']] = relationship('Order', back_populates='user')
    cart: Mapped['Cart'] = relationship('Cart', back_populates='user', uselist=False)
