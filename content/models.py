import os

from django.utils import timezone
from django.db import models

from imagefield.fields import ImageField


class Photo(models.Model):
    image = ImageField(
        'My Image', upload_to='photos', auto_add_fields=True, formats={
            f'c{width}x{width}': ['default', ('crop', (width, width))]
            for width in [144, 204, 226, 274, 320, 370, 450]
        }
    )
