import base64
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import requests


def img_size_reducer(image_data, name, resume_number):

    format, imgstr = image_data.split(';base64,')
    ext = format.split('/')[-1]
    image = ContentFile(base64.b64decode(
        imgstr), name='user_img_' + name + '_' + resume_number + '.' + ext)
    image = ImageFile(image)
    img_name = image.name
    image = Image.open(image)
    height, width = image.size
    if height > 300 or width > 300:
        new_size = (300, 300)
        image.thumbnail(new_size)
    buffer = BytesIO()
    image.save(fp=buffer, format=image.format)
    image = ContentFile(buffer.getvalue())
    image = InMemoryUploadedFile(
        image,       # file
        None,               # field_name
        img_name,           # file name
        'image/jpeg',       # content_type
        image.tell,  # size
        None)
    return image


def imgpath_to_base64(imgpath):
    image = 'http://127.0.0.1:8000'+imgpath
    base64img = base64.b64encode(requests.get(image).content)
    return base64img
