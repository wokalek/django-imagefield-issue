from content.models import Photo as PhotoModel


class Photo(PhotoModel):
    class Meta:
        proxy = True
