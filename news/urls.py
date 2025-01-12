from django.urls import path
from .views import PostsList, PostDetail, SearchPost, PostCreate, PostUpdate, PostDelete, Index
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', cache_page(60)(PostsList.as_view()), name='post_list'),
   path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
   path('search/', SearchPost.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='post_create_n'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/create/', PostCreate.as_view(), name='post_create_a'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
   path('time_zone', Index.as_view(), name='time_zone'),
]
