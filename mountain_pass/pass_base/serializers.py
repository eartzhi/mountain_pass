from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['email', 'phone', 'fam', 'name', 'otc']


class CoordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class PerevalImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ['per_image_name', 'per_image']


class PerevalAddedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_user', 'coords', 'winter']

        beauty_title = models.CharField(max_length=2, choices=BEAUTY_CHOICE,
                                        default='NI')
        title = models.TextField()
        other_titles = models.TextField()
        connect = models.TextField(default='')
        add_time = models.DateTimeField(auto_now_add=True)
        add_user = models.ForeignKey(Author, on_delete=models.CASCADE)
        coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
        winter = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                                  default='NI')
        summer = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                                  default='NI')
        autumn = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                                  default='NI')
        spring = models.CharField(max_length=2, choices=LEVEL_CHOICE,
                                  default='NI')
        add_image = models.ForeignKey(PerevalImages, on_delete=models.CASCADE)
        status = models.CharField(choices=STATUS_CHOICE, max_length=3)
        spr_activities_types = models.CharField(max_length=2,
                                                choices=ACTIVITIES_CHOICE,
                                                default='1')