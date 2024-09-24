from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter, CharFilter
from django.forms import DateTimeInput
from .models import Category


class PostFilter(FilterSet):
    heading = CharFilter(
        field_name='heading',
        lookup_expr='icontains',
        label='Название заголовка'
    )

    post_category = ModelMultipleChoiceFilter(
        field_name='post_category',
        queryset=Category.objects.all(),
        label='Категория'
    )

    pub_date = DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Дата',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
