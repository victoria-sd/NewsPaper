from django.contrib import admin
from .models import Author, Post, PostCategory, Category, Comment
from modeltranslation.admin import TranslationAdmin


class PostAdmin(TranslationAdmin):
    model = Post


class CategoryAdmin(TranslationAdmin):
    model = Category


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
