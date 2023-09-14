import json
from rest_framework.test import APIRequestFactory, APITransactionTestCase
from django.urls import reverse
from rest_framework import status

from .models import *
from .views import SubmitData


class TestSimple(APITransactionTestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SubmitData.as_view()
        self.my_url = '/SubmitData/'
        start_data_1 = {
                "beauty_title": "NI",
                "title": "start_title1",
                "other_titles": "start_other_title1",
                "connect": "",
                "author": {
                  "email": "abc01@yandex.ru",
                  "phone": "74951111111",
                  "fam": "Первов",
                  "name": "Один",
                  "otc": "Одинович"
                         },
                "coords": {
                  "latitude": 01.98805,
                  "longitude": 01.92527,
                  "height": 10011
                          },
                "level": {
                  "winter": "NI",
                  "summer": "NI",
                  "autumn": "NI",
                  "spring": "NI"
                        },
                "image": [
                        {
                    "image_name": "Стартовая вершина 1",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Стартовая вершина 2",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "NEW",
                "spr_activities_types": "3"
               },

        start_data_2 = {
                "beauty_title": "NI",
                "title": "start_title2",
                "other_titles": "start_other_title2",
                "connect": "",
                "author": {
                  "email": "abc02@yandex.ru",
                  "phone": "74952222222",
                  "fam": "Второв",
                  "name": "Два",
                  "otc": "Двович"
                         },
                "coords": {
                  "latitude": 02.988056,
                  "longitude": 02.925278,
                  "height": 20022
                          },
                "level": {
                  "winter": "IO",
                  "summer": "IO",
                  "autumn": "IO",
                  "spring": "IO"
                        },
                "image": [
                        {
                    "image_name": "Стартовая вершина 1",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Стартовая вершина 2",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "ACC",
                "spr_activities_types": "3"
               },

        start_data_1 = json.dumps(start_data_1)
        start_data_2 = json.dumps(start_data_2)

        response_1 = self.client.post(self.my_url, json=start_data_1)
        print(Pereval.objects.last())
        response_2 = self.client.post(self.my_url, json=start_data_2)

        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEquals(Pereval.objects.all().count(), 2)

    def test_pereval_addition(self):
        data_1 = {
                "beauty_title": "NI",
                "title": "test_title1",
                "other_titles": "test_other_title1",
                "connect": "",
                "author": {
                  "email": "abc1@yandex.ru",
                  "phone": "74951234567",
                  "fam": "Иванов",
                  "name": "Иван",
                  "otc": "Иванович"
                         },
                "coords": {
                  "latitude": 11.988056,
                  "longitude": 11.925278,
                  "height": 11111
                          },
                "level": {
                  "winter": "NI",
                  "summer": "NI",
                  "autumn": "NI",
                  "spring": "NI"
                        },
                "image": [
                        {
                    "image_name": "Тестовая вершина 1",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Тестовая вершина 2",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "NEW",
                "spr_activities_types": "1"
               },
        data_2 = {
                "beauty_title": "NI",
                "title": "test_title2",
                "other_titles": "test_other_title2",
                "connect": "",
                "author": {
                  "email": "abc2@yandex.ru",
                  "phone": "74957654321",
                  "fam": "Петров",
                  "name": "Петр",
                  "otc": "Петрович"
                         },
                "coords": {
                  "latitude": 22.988056,
                  "longitude": 22.925278,
                  "height": 22222
                          },
                "level": {
                  "winter": "PS",
                  "summer": "PS",
                  "autumn": "PS",
                  "spring": "PS"
                        },
                "image": [
                        {
                    "image_name": "Тестовая вершина 3",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Тестовая вершина 4",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "NEW",
                "spr_activities_types": "2"
               },

        response_1 = self.client.post(url=self.my_url,
                                    json=data_1)
        response_2 = self.client.post(url=self.my_url,
                                    json=data_2)

        new_pass = Pereval.objects.last()
        self.assertEquals(Pereval.objects.count(), 4)
        self.assertEqual(new_pass.title, 'test_title2')
        self.assertEqual(new_pass.other_titles, 'test_other_title2')
        self.assertEqual(new_pass.status, 'NEW')


