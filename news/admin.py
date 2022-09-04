from django.contrib import admin
from .models import Link, News, Photo, Message, Mark
# Register your models here.
admin.site.register(Link)
admin.site.register(News)
admin.site.register(Photo)
admin.site.register(Message)
admin.site.register(Mark)

