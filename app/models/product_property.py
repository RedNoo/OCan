from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime, ForeignKey

class ProductProperty(Base):
    __tablename__ = "product_properties"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    
    created_at : Mapped[datetime]  = mapped_column(DateTime(timezone=True),default=datetime.now())
    created_id : Mapped[int] = mapped_column(nullable=False)
    updated_at : Mapped[datetime]  = mapped_column(nullable=True)
    updated_id : Mapped[int] = mapped_column(nullable=False)

    product: Mapped['Product'] = relationship('Product')