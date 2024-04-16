from rest_framework import serializers
from blog .models import Post, Tag, Comment

from . import utils


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    post_title = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("post_title", "content", "author", "created")

    def get_post_title(self, obj):
        return obj.post.title


class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    author = serializers.CharField(source='author.username', read_only=True)
    html_content = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'author', 'excerpt',
                  'html_content', 'image', 'slug', 'published', 'comments', 'tags')

    # parse html content from ckeditor - Add absolute path to image tag
    def get_html_content(self, post):
        if post.content:
            request = self.context.get('request')
            if request:
                return utils.replace_relative_paths_with_absolute(request, post.content)
        return None
