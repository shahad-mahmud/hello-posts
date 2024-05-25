from pydantic import BaseModel, Field


class PostDetails(BaseModel):
    id: int
    title: str
    content: str
    author_id: int


class AllPostsResponse(BaseModel):
    message: str
    data: list[PostDetails] | None


class PostCreateRequest(BaseModel):
    title: str = Field(..., min_length=8, max_length=128, example="My First Post")
    content: str = Field(
        ...,
        min_length=8,
        max_length=1024,
        example="This is the content of my first post",
    )
    author_id: int = Field(..., example=1)
