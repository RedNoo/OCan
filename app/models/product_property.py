from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db import Base
from sqlalchemy import DateTime

class ProductProperty(Base):
    __tablename__ = "product_properties"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    created_at : Mapped[datetime]  = mapped_column(DateTime(timezone=True),default=datetime.now())

   