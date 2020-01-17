from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from movies.models import Actor, Movie


class MoviesTests(APITestCase):
    def setUp(self):
        self.emma = Actor.objects.create(
            name='Emma Watson',
            birth_date='1990-04-15',
        )

        self.hp = Movie.objects.create(
            name='Harry Potter',
            debut_date='2001-11-23',
            censorship='UC',
            direction='Chris Columbus',
        )
        self.hp.cast.set([self.emma.pk])
        self.hp.save()

        self.jw = Movie.objects.create(
            name='Jhon Wick 2',
            debut_date='2017-02-16',
            censorship='CE',
            direction='Chad Stahelski',
        )

    def test_create_movie(self):
        url = reverse('movie-list')

        name = 'Jhon Wick 3'
        data = {
            'name': name,
            'debut_date': '2019-05-16',
            'censorship': 'CE',
            'direction': 'Chad Stahelski',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 3)
        self.assertEqual(len(Movie.objects.filter(name=name)), 1)

    def test_name_is_unique(self):
        url = reverse('movie-list')

        data = {
            'name': 'Harry Potter',
            'debut_date': '2011-07-15',
            'censorship': 'UC',
            'direction': 'David Yates',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Movie.objects.count(), 2)

    def test_can_create_with_cast(self):
        url = reverse('movie-list')

        data = {
            'name': 'HP: Deathly Hallows 2',
            'debut_date': '2011-07-15',
            'censorship': 'CE',
            'direction': 'David Yates',
            'cast': [
                self.emma.pk,
            ],
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_get_all(self):
        url = reverse('movie-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_can_get_censored(self):
        url = reverse('movie-lists', args=['CE'])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_get_uncensored(self):
        url = reverse('movie-lists', args=['UC'])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_list_by_pk(self):
        url = reverse('movie-detail', args=[self.hp.pk])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.hp.pk)

    def test_can_update(self):
        url = reverse('movie-detail', args=[self.hp.pk])

        new_name = 'Harry Potter and the Philosopher\'s Stone'
        new_data = {
            'name': new_name,
        }

        response = self.client.patch(url, data=new_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Movie.objects.filter(name=new_name)), 1)

    def test_can_delete(self):
        url = reverse('movie-detail', args=[self.hp.pk])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 1)
