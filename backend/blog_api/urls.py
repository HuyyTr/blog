from django.urls import path
from .views import PostList, PostDetail, PostSearching


app_name = 'blog_api'

urlpatterns = [
    path('post/', PostList.as_view(), name='listcreate'),  # Post list
    path('post/<int:pk>/', PostDetail.as_view(),
         name='detailcreate'),  # Post detail
    path('post/search/', PostSearching.as_view(), name='postsearch')
]
