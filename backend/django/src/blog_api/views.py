from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import response, status
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from blog.models import Post

from .serializers import PostSerializer
from .filters import PostFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status='published', active=True)
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PostFilter
    search_fields = ["category__name", "title"]
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == "list":
            return (permissions.AllowAny(),)
        else:
            return (permissions.IsAuthenticated(),)

    @method_decorator(cache_page(60*15))
    def list(self, request):
        return super().list(request)

    @action(methods=['post'], detail=True, url_path='hide-post', url_name='hide-post')
    def hide_post(self, request, pk):
        try:
            p = Post.objects.get(pk=pk)
            p.active = False
            p.save()
        except Post.DoesNotExist:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        return response.Response(PostSerializer(p, context={'request': request}).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='show-post', url_name='show-post')
    def show_post(self, request, pk):
        try:
            p = Post.objects.get(pk=pk)
            p.active = True
            p.save()
        except Post.DoesNotExist:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        return response.Response(PostSerializer(p, context={'request': request}).data, status=status.HTTP_200_OK)
