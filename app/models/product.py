from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime, ForeignKey


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    name_seo: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now()
    )
    created_id: Mapped[int] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(nullable=True)
    updated_id: Mapped[int] = mapped_column(nullable=False)

    properties: Mapped[list["ProductProperty"]] = relationship(
        "ProductProperty", back_populates="product"
    )

    product_category: Mapped[list["ProductCategory"]] = relationship(
        "ProductCategory", back_populates="products"
    )
