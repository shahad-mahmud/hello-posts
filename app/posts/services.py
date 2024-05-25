from app.database import Post, User, execute, fetch_all, fetch_one

from .exceptions import AuthorNotFound
from .schemas import PostCreateRequest


def get_post_details(author_id: int = None):
    query = Post.__table__.select()

    if author_id:
        query = query.where(Post.author_id == author_id)

    return fetch_all(query)


def create_new_post(post: PostCreateRequest):
    user = fetch_one(User.__table__.select().where(User.id == post.author_id))
    if not user:
        raise AuthorNotFound()

    return execute(
        Post.__table__.insert().values(
            title=post.title,
            content=post.content,
            author_id=post.author_id,
        )
    )
