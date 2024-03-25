from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import ckeditor.fields as ckeditor_field


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='posts', default=1)
    title = models.CharField(max_length=250)
    tags = models.ManyToManyField(
        'Tag', related_name='posts', blank=True)
    excerpt = models.TextField(null=True)
    content = ckeditor_field.RichTextField()
    image = models.ImageField(
        upload_to='images/%Y/%m/', default='no-image.jpg')
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=10, choices=options, default="published")

    class Meta:
        ordering = ('-published',)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.post.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
