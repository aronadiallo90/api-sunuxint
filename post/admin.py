from django.contrib import admin

# Register your models here.
# listings/admin.py

from django.contrib import admin

from post.models import Post

admin.site.register(Post)