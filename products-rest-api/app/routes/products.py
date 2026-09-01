from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/products")


# Listing All Products
@router.get("/")
def list_products():
    return [
        {"id": 134, "name": "iPhone 17", "price": 125000, "description": "..."},
        {
            "id": 135,
            "name": "Samsung Galaxy S30",
            "price": 115000,
            "description": "...",
        },
        {"id": 1, "name": "Laptop Bag", "price": 1250, "description": "..."},
    ]


# Creating a new product
@router.post("/")
def add_product(product: dict):
    print("About to add product")
    print(product)
    return {"id": 1000, "status": "Saved Successfully"}


# Retrieving a specific product with id
@router.get("/{product_id}")
def get_product_by_id(product_id: int):
    print(id)
    return {"id": product_id, "name": "Laptop Bag", "price": 1250, "description": "..."}


# updating product by id
@router.put("/{product_id}")
def update_product(product_id: int, product: dict):
    print("About to update product")
    print(f"Product ID: {product_id}")
    print(product)
    return {"id": product_id, "status": "Updated Successfully"}


# deleting product by id
@router.delete("/{product_id}")
def delete_product(product_id: int):
    print(f"Product ID: {product_id}")
    return {"id": product_id, "status": "Deleted Successfully"}


# deleting product in bulk
@router.delete("/")
def delete_product(product_ids: list[int]):
    print(f"Product IDs: {product_ids}")
    return {"status": "Deleted All Products Successfully"}
