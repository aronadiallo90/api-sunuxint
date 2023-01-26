from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework import generics
from rest_framework.response import Response
 
from post.models import Post
from post.serializers import PostSerializer
 
class PostAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Post.objects.all()
        serializer = PostSerializer(categories, many=True)
        return Response(serializer.data)
    
class PostCreateview(generics.CreateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer

class PostUpdateview(generics.UpdateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer

class PostDeleteView(generics.DestroyAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer