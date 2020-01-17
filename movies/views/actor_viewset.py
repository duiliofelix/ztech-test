from rest_framework import viewsets, filters

from movies.models import Actor
from movies.serializers.actor_serializer import ActorSerializer


class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
