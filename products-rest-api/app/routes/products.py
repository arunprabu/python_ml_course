from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/products")


# Let's handle GET request on localhost:8000/api/v1/products/
@router.get("/")
def list_products():
    print("About to list products")
    return [{"id": 134, "name": "iPhone 17", "price": 125000, "description": "..."}]


# Let's handle POST request on localhost:8000/api/v1/products
@router.post("/")
def add_product(product: dict):
    print("About to add product")
    print(product)
    return {"id": 1000, "status": "Saved Successfully"}
