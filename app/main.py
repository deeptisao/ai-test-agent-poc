from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from uuid import UUID, uuid4

app = FastAPI(
    title="AI Test Agent POC",
    description="FastAPI app for automated test generation using OpenAPI + LLMs",
    version="1.0.0"
)

# -----------------------------
# Models
# -----------------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr

class User(UserCreate):
    id: UUID

# -----------------------------
# In-memory DB (POC only)
# -----------------------------
db: dict[UUID, User] = {}

# -----------------------------
# Routes
# -----------------------------
@app.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    # simple duplicate check
    for u in db.values():
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(id=uuid4(), **user.dict())
    db[new_user.id] = new_user
    return new_user


@app.get("/users", response_model=List[User])
def list_users():
    return list(db.values())


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: UUID):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")
    return db[user_id]


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: UUID):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")
    del db[user_id]
    return None
