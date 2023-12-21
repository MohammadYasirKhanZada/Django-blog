from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# PostList View
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass

# PostDetail View
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass