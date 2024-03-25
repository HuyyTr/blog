from rest_framework import response, status
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .serializers import PostSerializer

from blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status='published', active=True)
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action == "list":
            return (permissions.AllowAny(),)
        else:
            return (permissions.IsAuthenticated(),)

    def list(self, request):
        queryset = self.get_queryset()
        query_params = request.query_params
        if query_params:
            if query_params.get('category'):
                category = query_params.get('category')
                queryset = queryset.filter(
                    category__name__icontains=category)
            elif query_params.get('slug'):
                slug = query_params.get('slug')
                queryset = queryset.filter(slug__icontains=slug)
            else:
                return response.Response(status=204)

        serializer = self.get_serializer(
            queryset, many=True, context={"request": request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)

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
