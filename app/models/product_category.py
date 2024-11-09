from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime, ForeignKey


class ProductCategory(Base):
    __tablename__ = "product_category"

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)

    products: Mapped['Product'] = relationship('Product')
    categories: Mapped['Category'] = relationship('Category')
