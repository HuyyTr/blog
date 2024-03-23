from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'author', 'excerpt',
                  'content', 'image', 'slug', 'status')
