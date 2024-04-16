import django_filters
from blog.models import Post


class PostFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category__name', lookup_expr='iexact')
    title = django_filters.CharFilter(
        field_name='title', lookup_expr='icontains')
    slug = django_filters.CharFilter(
        field_name='slug', lookup_expr="icontains"
    )

    class Meta:
        model = Post
        fields = ('category', 'title',)
