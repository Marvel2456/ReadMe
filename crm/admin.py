from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Story)
admin.site.register(Chapter)
admin.site.register(Comment)
admin.site.register(LikedStory)
admin.site.register(Review)
admin.site.register(Favorite)
