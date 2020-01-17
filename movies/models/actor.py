from django.db import models


class Actor(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
    )

    birth_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
