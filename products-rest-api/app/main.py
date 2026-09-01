from fastapi import FastAPI

# importing our newly created api routes
from app.routes import products

app = FastAPI(title="Products and Prediction REST API")

# registering the api endpoint
app.include_router(products.router)

# start the serv
# uv run uvicorn app.main:app --reload
