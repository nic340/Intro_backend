from sqlmodel import SQLModel, Field


# 1. USER MODEL
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str


# 2. PRODUCT MODEL
class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    stock: int


# 3. ORDER MODEL
class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    quantity: int
    total_price: float
    product_id: int | None = Field(default=None, foreign_key="product.id")
    user_id: int | None = Field(default=None, foreign_key="user.id")

