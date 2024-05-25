from pydantic import BaseModel, EmailStr


class UserDetails(BaseModel):
    id: int
    name: str
    email: str


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr


class UserDetailsResponse(BaseModel):
    message: str
    data: UserDetails | None


class AllUserDetailsResponse(BaseModel):
    message: str
    data: list[UserDetails]
