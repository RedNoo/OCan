from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_type : Mapped[int] = mapped_column(nullable=False, default=1)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created_at : Mapped[datetime]  = mapped_column(DateTime(timezone=True),default=datetime.now())
    created_ip_address : Mapped[str] = mapped_column(nullable=False) 
    last_login_date : Mapped[datetime] = mapped_column(nullable=True)
    last_login_ipaddress : Mapped[str] = mapped_column(nullable=True)
    number_of_invalid_login_attemps : Mapped[int] = mapped_column(nullable=False, default=0)
    status : Mapped[int] = mapped_column(nullable=False, default=1)


    orders: Mapped[list['Order']] = relationship('Order', back_populates='user')
    cart: Mapped['Cart'] = relationship('Cart', back_populates='user', uselist=False)
