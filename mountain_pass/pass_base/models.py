from django.db import models
from django.contrib.auth.models import User


class Coords(models.Model):
    latitude = models.FloatField(max_length=8)
    longitude = models.FloatField(max_length=8)
    height = models.IntegerField(max_length=4)


class PerevalImages(models.Model):
    name = models.CharField(max_length=50)
    photos = models.ImageField('Фото', upload_to='Pass_images',
                               blank=True)


class PerevalAdded(models.Model):
    BEAUTY_CHOICE = [
        ('NO_INFO', 'нет информации'),
        ('PS', 'Перевал'),
        ('TP', 'Вершина'),
        ('GL', 'Ледник'),
        ('IO', 'Объект инфраструктуры'),
        ('NO', 'Объект природы'),

    ]

    LEVEL_CHOICE = [
        ('NO_INFO', 'нет информации'),
        ('A1', '1А'),
        ('B1', '1Б'),
        ('А2', '2А'),
        ('В2', '2Б'),
        ('А3', '3А'),
        ('В3', '3Б'),
    ]

    beauty_title = models.CharField(max_length=2, choices=BEAUTY_CHOICE,
                                    default='NO_INFO')
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    add_user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    winter = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                              default='NO_INFO')
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                              default='NO_INFO')
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                              default='NO_INFO')
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                             default='NO_INFO')
    add_image = models.ForeignKey(PerevalImages, on_delete=models.CASCADE)





