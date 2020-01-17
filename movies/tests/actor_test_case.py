from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from movies.models import Actor


class ActorTests(APITestCase):
    def setUp(self):
        self.emma = Actor.objects.create(
            name='Emma Watson',
            birth_date='1990-04-15',
        )

    def test_create_actor(self):
        url = reverse('actor-list')

        name = 'Keanu Reeves'
        data = {
            'name': name,
            'birth_date': '1964-09-02',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.count(), 2)
        self.assertEqual(len(Actor.objects.filter(name=name)), 1)

    def test_name_is_unique(self):
        url = reverse('actor-list')

        data = {
            'name': 'Emma Watson',
            'birth_date': '1990-04-15',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Actor.objects.count(), 1)

    def test_can_get_all(self):
        url = reverse('actor-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_list_by_pk(self):
        url = reverse('actor-detail', args=[self.emma.pk])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.emma.pk)

    def test_can_update(self):
        url = reverse('actor-detail', args=[self.emma.pk])

        new_name = 'Emma'
        new_data = {
            'name': new_name,
        }

        response = self.client.patch(url, data=new_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Actor.objects.filter(name=new_name)), 1)

    def test_can_delete(self):
        url = reverse('actor-detail', args=[self.emma.pk])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Actor.objects.count(), 0)
