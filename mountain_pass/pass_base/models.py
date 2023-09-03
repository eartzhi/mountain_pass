from django.db import models


class Author(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    fam = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    otc = models.CharField(max_length=30)


class Coords(models.Model):
    latitude = models.FloatField(max_length=8)
    longitude = models.FloatField(max_length=8)
    height = models.IntegerField()


class PerevalImages(models.Model):
    per_image_name = models.TextField()
    per_image = models.ImageField('Фото', upload_to='Pass_images',
                               blank=True)


class Level(models.Model):
    LEVEL_CHOICE = [
        ('NI', 'нет информации'),
        ('A1', '1А'),
        ('B1', '1Б'),
        ('А2', '2А'),
        ('В2', '2Б'),
        ('А3', '3А'),
        ('В3', '3Б'),
    ]

    winter = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                              default='NI')
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                              default='NI')
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                              default='NI')
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                             default='NI')


class PerevalAdded(models.Model):
    BEAUTY_CHOICE = [
        ('NI', 'нет информации'),
        ('PS', 'Перевал'),
        ('TP', 'Вершина'),
        ('GL', 'Ледник'),
        ('IO', 'Объект инфраструктуры'),
        ('NO', 'Объект природы'),

    ]

    STATUS_CHOICE = [
        ('NEW', 'новый'),
        ('PEN', 'в работе'),
        ('ACC', 'принят'),
        ('REJ', 'отклонен'),
    ]

    ACTIVITIES_CHOICE = [
        ('1', 'пешком'),
        ('2', 'лыжи'),
        ('3', 'катамаран'),
        ('4', 'байдарка'),
        ('5', 'плот'),
        ('6', 'сплав'),
        ('7', 'велосипед'),
        ('8', 'автомобиль'),
        ('9', 'мотоцикл'),
        ('10', 'парус'),
        ('11', 'верхом'),
    ]

    beauty_title = models.CharField(max_length=2, choices=BEAUTY_CHOICE,
                                    default='NI')
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.TextField(default='')
    add_time = models.DateTimeField(auto_now_add=True)
    add_user = models.ForeignKey(Author, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    add_image = models.ForeignKey(PerevalImages, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=3,
                              default='NEW')
    spr_activities_types = models.CharField(max_length=2,
                                            choices=ACTIVITIES_CHOICE,
                                            default='1')
