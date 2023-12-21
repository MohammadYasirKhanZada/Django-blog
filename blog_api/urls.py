# All urls.py code will go here.
# Folder blog_api own urls.py file.

from django.urls import path
from .views import PostList, PostDetail

app_name = "blog_api"

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"),
    path('', PostList.as_view(), name='listcreate')
]
