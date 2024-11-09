from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime, ForeignKey

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    name_seo: Mapped[str] = mapped_column(nullable=False)

    product_category: Mapped[list["ProductCategory"]] = relationship(
        "ProductCategory", back_populates="categories"
    )



