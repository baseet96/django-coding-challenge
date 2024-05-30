from rest_framework.generics import ListCreateAPIView
from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.order_by("id")
        
        runtime_longer_than = self.request.query_params.get('runtime_longer_than', None)
        runtime_shorter_than = self.request.query_params.get('runtime_shorter_than', None)
        
        if runtime_longer_than is not None:
            queryset = queryset.filter(runtime__gt=runtime_longer_than)
        
        if runtime_shorter_than is not None:
            queryset = queryset.filter(runtime__lt=runtime_shorter_than)
        
        return queryset
