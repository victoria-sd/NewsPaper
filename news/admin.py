from django.contrib import admin
from .models import Author, Post, PostCategory, Category, Comment
from modeltranslation.admin import TranslationAdmin


class PostAdmin(TranslationAdmin):
    model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
