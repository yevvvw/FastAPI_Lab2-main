from fastapi import APIRouter

from models.common import AllUsersResponse, ActionResultResponse
from models.users import User

router = APIRouter(prefix="/api/users")
known_users: list[User] = []


@router.get("/")
def list_users() -> AllUsersResponse:
    return AllUsersResponse(users=known_users)


@router.put("/")
def edit_user(user: User) -> ActionResultResponse:
    for i, u in enumerate(known_users):
        if u.id == user.id:
            known_users[i] = user
            return ActionResultResponse(result=True)
    return ActionResultResponse(result=False)


@router.post("/")
def add_user(user: User) -> ActionResultResponse:
    known_users.append(user)
    return ActionResultResponse(result=True)


@router.get("/{user_id}")
def find_user(user_id: int) -> ActionResultResponse | User:
    for u in known_users:
        if u.id == user_id:
            return u
    return ActionResultResponse(result=False)


@router.delete("/{user_id}")
def delete_user(user_id: int) -> ActionResultResponse:
    for i, u in enumerate(known_users):
        if u.id == user_id:
            known_users.remove(u)
            return ActionResultResponse(result=True)
    return ActionResultResponse(result=False)
