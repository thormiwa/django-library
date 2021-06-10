from django.db.models import fields
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ('name', )

class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = models.Book
        fields = (
            'title', 'description', 'image', 'author'
        )

class RentSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=True, read_only=True)
    book = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Rent
        fields = ('reason', 'return_date', 'user', 'book', )

class ReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=True, read_only=True)
    book = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Review
        fields = ('comment', 'rate', 'user', 'book', )

