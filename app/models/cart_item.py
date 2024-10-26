from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime, ForeignKey
from app.models import Product, Cart

class CartItem(Base):
    __tablename__ = 'cart_items'
    id: Mapped[int] = mapped_column(primary_key=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    quantity: Mapped[int] = mapped_column(nullable=False)

    cart: Mapped['Cart'] = relationship('Cart', back_populates='cart_items')
    product: Mapped['Product'] = relationship('Product')