from fastapi import APIRouter


posts_router = APIRouter(prefix='/posts', tags=['Posts'])

from user_posts import user_post_api