from pydantic import BaseModel, EmailStr, Field


class UserDetails(BaseModel):
    id: int
    name: str
    email: str


class CreateUserRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=128)
    email: EmailStr


class UserDetailsResponse(BaseModel):
    message: str
    data: UserDetails | None


class AllUserDetailsResponse(BaseModel):
    message: str
    data: list[UserDetails]
