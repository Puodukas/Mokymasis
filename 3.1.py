from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///3_uzd.db')
Base = declarative_base()


class Apparel_Size(Base):
    __tablename__ = "Apparel Size"
    size_id = Column("size id", Integer, primary_key=True)
    size_code = Column("size code", Integer)
    sort_order = Column("sort Order", String)


class Product(Base):
    __tablename__ = "Product"
    product_name = Column("product name", String)
    product_id = Column("product id", Integer, primary_key=True)
    other_data = Column("Other data", String)


class Product_Categories(Base):
    __tablename__ = "Product Categories"
    category_id = Column("category id", Integer, primary_key=True)


class Categories(Base):
    __tablename__ = "Categories"
    parent_category_id = Column("parent category id", Integer)
    category_name = Column("category name", String)
    category_id = Column("category id", Integer, primary_key=True)


class Color(Base):
    __tablename__ = "Color"
    color_id = Column("color id", Integer, primary_key=True)
    color_code = Column("Color code", Integer)
    color_name = Column("Color name", String)
    # id = relationship("Product Colors") neveik kazkas


class Product_Colors(Base):
    __tablename__ = "Product Colors"
    id = Column("id", Integer, primary_key=True)
    # color_id = Column(Integer, ForeignKey("Color.id"))


Base.metadata.create_all(engine)
