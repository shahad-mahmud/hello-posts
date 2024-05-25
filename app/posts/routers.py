from fastapi import APIRouter, status

from .schemas import AllPostsResponse, PostCreateRequest
from .services import create_new_post, get_post_details

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=AllPostsResponse)
def list_posts():
    data = get_post_details()

    if not data:
        return {"message": "no posts found", "data": None}

    return {"message": "fetched all posts", "data": data}


@router.get(
    "/{author_id}", status_code=status.HTTP_200_OK, response_model=AllPostsResponse
)
def list_posts_by_author(author_id: int):
    data = get_post_details(author_id)

    if not data:
        return {"message": "no posts found", "data": None}

    return {"message": "fetched all posts", "data": data}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def create_post(payload: PostCreateRequest):
    create_new_post(payload)

    return {"message": "post created successfully"}
