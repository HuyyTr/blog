from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer

from blog.models import Post


# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostSearching(APIView):
    def get(self, request):
        queryset: any
        if request.query_params.get('category'):
            category = request.query_params.get('category')
            queryset = Post.post_objects.filter(
                category__name__icontains=category)
        elif request.query_params.get('slug'):
            slug = request.query_params.get('slug')
            queryset = Post.post_objects.filter(slug__icontains=slug)
        else:
            return Response({'error': 'Filter parameter is missing or not valid'}, status=400)

        if not queryset.exists():
            return Response({'message': 'Queryset is empty'}, status=204)

        serializer = PostSerializer(
            queryset, many=True, context={"request": request})
        return Response(serializer.data)
