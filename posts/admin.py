from django.contrib import admin

from posts.models import *

admin.site.register(Language)
admin.site.register(TextPost)
admin.site.register(VideoPost)
admin.site.register(BookPost)

