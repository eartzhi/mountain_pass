from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['email',
                  'phone',
                  'fam',
                  'name',
                  'otc'
                  ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude',
                  'longitude',
                  'height'
                  ]


class PerevalImagesSerializer(serializers.ModelSerializer):
    per_image = serializers.URLField()

    class Meta:
        model = PerevalImages
        fields = ['per_image_name',
                  'per_image'
                  ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter',
                  'summer',
                  'autumn',
                  'spring'
                  ]


class PerevalAddedSerializer(WritableNestedModelSerializer):
    add_user = AuthorSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    add_image = PerevalImagesSerializer(many=True, allow_null=True)

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

    # def create(self, validated_data, **kwargs):
    #     images = validated_data.pop('add_image')
    #     if images:
    #         for image in images:
    #             name = image.pop('per_image_name')
    #             photos = photos.pop(photos)
    #             PerevalImages.objects.create(perevall=perevall, name=name, photo=photos)

