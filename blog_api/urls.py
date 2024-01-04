# All urls.py code will go here.
# Folder blog_api own urls.py file.
# this is app-level urls.py which contains router or urls patterns  whcih are specific for app ie blog_api folder.
from django.urls import path
from .views import PostList, PostDetail

app_name = "blog_api"

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"),
    path('', PostList.as_view(), name='listcreate')
]
