from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'slug', 'intro', 'date_add')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comm', 'user', 'date_add')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
