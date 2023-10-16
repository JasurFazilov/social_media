from fastapi import APIRouter


profile_router = APIRouter(prefix='/profile', tags=['Profiles'])

from profile import profile_api

