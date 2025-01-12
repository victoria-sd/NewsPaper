from .models import Post, Category
from modeltranslation.translator import register, TranslationOptions


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('heading', 'content')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name_category', )
