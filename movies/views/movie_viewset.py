from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers.movie_serializer import MovieSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    @action(methods=['GET'], detail=False, url_path='lists/(?P<censorship>[^/.]+)')
    def lists(self, request, censorship=Movie.CENSORED):
        movie_list = self.queryset.filter(censorship=censorship)
        serializer = self.get_serializer(movie_list, many=True)

        return Response(serializer.data)
