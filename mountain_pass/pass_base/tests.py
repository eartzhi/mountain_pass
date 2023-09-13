from django.test import TestCase



class SimpleTest(TestCase):

    def pereval_addition(self):
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


