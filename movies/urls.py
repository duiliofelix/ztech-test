from django.conf.urls import include, url
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register(r'actors', views.ActorsViewSet)
router.register(r'', views.MoviesViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
