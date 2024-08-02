from django.contrib import admin
from django.forms import TextInput, ModelForm

from content.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Photo, PhotoAdmin)
