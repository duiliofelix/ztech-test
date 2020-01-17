from rest_framework import serializers

from movies.models import Actor, Movie


class MovieSerializer(serializers.ModelSerializer):
    cast = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
        required=False,
    )

    class Meta:
        model = Movie
        fields = '__all__'
