from django.db import models

from .actor import Actor


class Movie(models.Model):
    CENSORED = 'CE'
    UNCENSORED = 'UC'

    CensorshipChoices = (
        (CENSORED, 'Censored'),
        (UNCENSORED, 'Uncensored'),
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    debut_date = models.DateField()

    censorship = models.CharField(
        max_length=2,
        choices=CensorshipChoices,
    )

    direction = models.CharField(
        max_length=100,
    )

    cast = models.ManyToManyField(
        Actor,
        related_name='movies',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
