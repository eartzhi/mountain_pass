from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['email',
                  'phone',
                  'fam',
                  'name',
                  'otc'
                  ]


class CoordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude',
                  'longitude',
                  'height'
                  ]


class PerevalImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ['per_image_name',
                  'per_image'
                  ]


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ['winter',
                  'summer',
                  'autumn',
                  'spring'
                  ]


class PerevalAddedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'add_user',
                  'coords',
                  'level',
                  'add_image',
                  'status',
                  'spr_activities_types'
                  ]

