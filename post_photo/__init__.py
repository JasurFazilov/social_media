from fastapi import APIRouter, UploadFile


photo_router = APIRouter(prefix='/photo', tags=['Photos'])

from post_photo import post_photo_api


# example
# @photo_router.post('/upload-photo')
# async def upload_photo_api(post_id: int, photo_file: UploadFile):
#     with open('media/image.jpg', 'wb') as new_photo:
#         front_file_read = await photo_file.read()
#         new_photo.write(front_file_read)
#
#     return {'message': 'Photo added'}
#
#
# @photo_router.get('/get-photo')
# async def get_photo_url():
#     pass

