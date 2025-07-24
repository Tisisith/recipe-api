from crud.user import get_user_by_username, create_user
from schemas.user import UserCreate

def register_user(user: UserCreate, db):
    if get_user_by_username(db, user.username):
        raise ValueError("Username already taken")
    return create_user(db, user)