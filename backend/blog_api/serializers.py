from rest_framework import serializers
from blog .models import Post, Tag

from . import utils


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    html_content = serializers.SerializerMethodField()
    category = serializers.CharField(source='category.name', read_only=True)
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'author', 'excerpt',
                  'html_content', 'image', 'slug', 'published', 'tags')

    # parse html content from ckeditor - Add absolute path to image tag
    def get_html_content(self, post):
        if post.content:
            request = self.context.get('request')
            if request:
                return utils.replace_relative_paths_with_absolute(request, post.content)
        return None
