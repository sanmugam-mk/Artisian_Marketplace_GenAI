from sqlalchemy import Column, Integer, String, Text

from database import Base

class ProductContent(Base):
    __tablename__ = "product_content"

    id = Column(Integer, primary_key=True, index=True)

    product = Column(String)
    material = Column(String)
    craft_type = Column(String)
    region = Column(String)

    description = Column(Text)
    details = Column(Text)
    pricing = Column(Text)