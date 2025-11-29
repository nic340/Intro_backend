from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from database import create_db_and_tables, engine
from models import Store, Transaction, Fee
from contextlib import asynccontextmanager

# Lifecycle manager to create tables on startup [cite: 265]
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# ==========================================
#  STORE CRUD
# ==========================================

# Create Store
@app.post("/stores/")
def create_store(store: Store):
    with Session(engine) as session:
        session.add(store)
        session.commit()
        session.refresh(store)
        return store

# Read All Stores
@app.get("/stores/")
def read_stores():
    with Session(engine) as session:
        statement = select(Store)
        results = session.exec(statement).all()
        return results

# Read One Store
@app.get("/stores/{store_id}")
def read_store(store_id: int):
    with Session(engine) as session:
        store = session.get(Store, store_id)
        if not store:
            raise HTTPException(status_code=404, detail="Store not found")
        return store

# Update Store
@app.put("/stores/{store_id}")
def update_store(store_id: int, store_data: Store):
    with Session(engine) as session:
        store = session.get(Store, store_id)
        if not store:
            raise HTTPException(status_code=404, detail="Store not found")
        store.name = store_data.name
        store.address = store_data.address
        session.add(store)
        session.commit()
        session.refresh(store)
        return store

# Delete Store
@app.delete("/stores/{store_id}")
def delete_store(store_id: int):
    with Session(engine) as session:
        store = session.get(Store, store_id)
        if not store:
            raise HTTPException(status_code=404, detail="Store not found")
        session.delete(store)
        session.commit()
        return {"message": "Store deleted successfully"}

# ==========================================
#  TRANSACTION CRUD
# ==========================================

# Create Transaction
@app.post("/transactions/")
def create_transaction(transaction: Transaction):
    with Session(engine) as session:
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction

# Read All Transactions
@app.get("/transactions/")
def read_transactions():
    with Session(engine) as session:
        statement = select(Transaction)
        results = session.exec(statement).all()
        return results

# Read One Transaction
@app.get("/transactions/{transaction_id}")
def read_transaction(transaction_id: int):
    with Session(engine) as session:
        transaction = session.get(Transaction, transaction_id)
        if not transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return transaction

# Update Transaction Status
@app.patch("/transactions/{transaction_id}")
def update_transaction_status(transaction_id: int, status: str):
    with Session(engine) as session:
        transaction = session.get(Transaction, transaction_id)
        if not transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        transaction.status = status
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction

# Delete Transaction
@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):
    with Session(engine) as session:
        transaction = session.get(Transaction, transaction_id)
        if not transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        session.delete(transaction)
        session.commit()
        return {"message": "Transaction deleted"}

# ==========================================
#  FEE CRUD
# ==========================================

# Create Fee
@app.post("/fees/")
def create_fee(fee: Fee):
    with Session(engine) as session:
        session.add(fee)
        session.commit()
        session.refresh(fee)
        return fee

# Read Fee by Transaction ID
@app.get("/fees/{transaction_id}")
def read_fee(transaction_id: int):
    with Session(engine) as session:
        statement = select(Fee).where(Fee.transaction_id == transaction_id)
        result = session.exec(statement).first()
        if not result:
            raise HTTPException(status_code=404, detail="Fee not found")
        return result

# Delete Fee
@app.delete("/fees/{fee_id}")
def delete_fee(fee_id: int):
    with Session(engine) as session:
        fee = session.get(Fee, fee_id)
        if not fee:
            raise HTTPException(status_code=404, detail="Fee not found")
        session.delete(fee)
        session.commit()
        return {"message": "Fee deleted"}
