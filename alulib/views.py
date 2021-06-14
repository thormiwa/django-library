from rest_framework import generics
from rest_framework import filters
from . import models
from . import serializers

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class BookList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter, )
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer