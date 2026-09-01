from fastapi import FastAPI

# importing our newly created api routes
from app.routes import products
from app.routes import predict

app = FastAPI()


@app.get("/")
def read_home():
    return {"message": "Welcome to Home Page!"}


@app.get("/about")
def read_about():
    return {"message": "Welcome to About Page!"}


@app.get("/contact")
def read_contact():
    return {"message": "Welcome to Contact Page!"}


# registering the api endpoint
app.include_router(products.router)
app.include_router(predict.router)
