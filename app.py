from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from database import create_db_and_tables, engine
from models import User, Product, Order
from contextlib import asynccontextmanager


# LIFECYCLE
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

# ==================================================
# USER CRUD
# ==================================================

@app.post("/users/")
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


@app.get("/users/")
def read_users():
    with Session(engine) as session:
        return session.exec(select(User)).all()


@app.get("/users/{user_id}")
def read_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(404, "User not found")
        return user


@app.put("/users/{user_id}")
def update_user(user_id: int, data: User):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(404, "User not found")
        user.name = data.name
        user.email = data.email
        session.commit()
        session.refresh(user)
        return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(404, "User not found")
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully"}


# ==================================================
# PRODUCT CRUD
# ==================================================

@app.post("/products/")
def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product


@app.get("/products/")
def read_products():
    with Session(engine) as session:
        return session.exec(select(Product)).all()


@app.get("/products/{product_id}")
def read_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(404, "Product not found")
        return product


@app.put("/products/{product_id}")
def update_product(product_id: int, data: Product):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(404, "Product not found")
        product.name = data.name
        product.price = data.price
        product.stock = data.stock
        session.commit()
        session.refresh(product)
        return product


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(404, "Product not found")
        session.delete(product)
        session.commit()
        return {"message": "Product deleted"}


# ==================================================
# ORDER CRUD
# ==================================================

@app.post("/orders/")
def create_order(order: Order):
    with Session(engine) as session:
        session.add(order)
        session.commit()
        session.refresh(order)
        return order


@app.get("/orders/")
def read_orders():
    with Session(engine) as session:
        return session.exec(select(Order)).all()


@app.get("/orders/{order_id}")
def read_order(order_id: int):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        if not order:
            raise HTTPException(404, "Order not found")
        return order


@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        if not order:
            raise HTTPException(404, "Order not found")
        session.delete(order)
        session.commit()
        return {"message": "Order deleted"}
04, detail="Fee not found")
        session.delete(fee)
        session.commit()
        return {"message": "Fee deleted"}
