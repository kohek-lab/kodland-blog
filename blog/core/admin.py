from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_body', 'post_image', 'creation_date')


admin.site.register(Post, PostAdmin)
