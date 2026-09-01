from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/users")


@router.get("/")
def list_users():
    return [{"id": 134, "name": "John Doe", "email": "john.doe@example.com"}]


@router.post("/")
def add_user(user: dict):
    print("About to add user")
    print(user)
    return {"id": 1000, "status": "Saved Successfully"}
