from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['heading', 'content', 'post_category', 'post_author']
        labels = {
            'heading': 'Заголовок',
            'content': 'Текст',
            'post_category': 'Категория',
            'post_author': 'Автор'
        }

