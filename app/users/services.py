from app.database import User, execute, fetch_all, fetch_one
from app.users.exceptions import EmailAlreadyExists
from app.users.schemas import CreateUserRequest


def get_user_details_service(id: int = None):
    query = User.__table__.select()
    if id:
        query = query.where(User.id == id)
        return fetch_one(query)

    return fetch_all(query)


def create_user_service(user: CreateUserRequest):
    query = User.__table__.select().where(User.email == user.email)
    db_user = fetch_one(query)

    if db_user:
        return EmailAlreadyExists()

    query = User.__table__.insert().values(**user.model_dump())

    return execute(query)
