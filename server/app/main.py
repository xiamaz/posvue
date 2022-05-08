from fastapi import FastAPI, Depends

from .dependencies.auth import get_current_active_user
from .schemas.user import User
from .routers import token

app = FastAPI()

app.include_router(token.router)

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
