from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter, CharFilter
from django.forms import DateTimeInput
from .models import Category
from django.utils.translation import gettext as _


class PostFilter(FilterSet):
    heading = CharFilter(
        field_name='heading',
        lookup_expr='icontains',
        label=_('Title')
    )

    post_category = ModelMultipleChoiceFilter(
        field_name='post_category',
        queryset=Category.objects.all(),
        label=_('Category')
    )

    pub_date = DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        label=_('Data'),
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
