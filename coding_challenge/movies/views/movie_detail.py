from rest_framework.generics import RetrieveUpdateDestroyAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer