from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    name_seo: Mapped[str] = mapped_column(nullable=False)
    order_id: Mapped[int] = mapped_column(nullable=False, default=0)

    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="categories"
    )
