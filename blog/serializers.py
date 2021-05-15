from rest_framework import serializers
from .models import Post, Comments 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'post_date', 'category']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['post','name','body','date_added']
