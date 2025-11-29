from sqlmodel import Field, SQLModel

# 1. Store Model
class Store(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str

# 2. Transaction Model
class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    gcash_number: str
    amount: float
    status: str
    # Foreign Key linking to Store
    store_id: int | None = Field(default=None, foreign_key="store.id")

# 3. Fee Model
class Fee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    fee_percentage: float
    fee_amount: float
    # Foreign Key linking to Transaction (One-to-One concept)
    transaction_id: int | None = Field(default=None, foreign_key="transaction.id")
