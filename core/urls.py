# this is Project level urls.py which contains urls for entire django projects.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('api/', include('blog_api.urls' ,namespace='blog_api'))
]
