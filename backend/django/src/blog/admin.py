from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
from . import forms


class CommentInline(admin.StackedInline):
    model = models.Comment
    fk_name = 'post'


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    form = forms.PostForm
    inlines = (CommentInline,)

    list_display = ('title', 'category', 'status', 'author', 'get_tags')
    search_fields = ('title', 'status', 'category__name')
    list_filter = ('category', 'tags__name')
    prepopulated_fields = {'slug': ('title',), }

    readonly_fields = ('avatar',)

    @admin.display(description="tags")
    def get_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])

    @admin.display(description="avatar")
    def avatar(self, post):
        return mark_safe("<img src='/media/{image_url}' alt={alt} width='120px'/>".format(image_url=post.image, alt=post.title))


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created')
    search_fields = ('post__title',)
    list_filter = ('post',)


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Comment, CommentAdmin)
