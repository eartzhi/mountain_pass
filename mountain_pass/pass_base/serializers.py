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


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['image_name',
                  'image'
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
    # author = AuthorSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    image = ImagesSerializer(many=True, allow_null=True)

    class Meta:
        model = PerevalAdded
        fields = ['beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'author',
                  'coords',
                  'level',
                  'image',
                  'status',
                  'spr_activities_types'
                  ]

    def create(self, validated_data, **kwargs):
        author = validated_data.pop('author')
            # coords = validated_data.pop('coords')
            # level = validated_data.pop('level')
            # images = validated_data.pop('image')

        current_author = Author.objects.filter(email=author['email'])
        if current_author.exists():
            pereval = PerevalAdded.objects.create(**validated_data,
                                                  author=current_author,
                                                  )
            # author_serializer = AuthorSerializer(data=author)
            # author_serializer.is_valid(raise_exception=True)
            # author = author_serializer.save()
        else:
            author = Author.objects.create(**author)

            # coords = Coords.objects.create(**coords)
            # level = Level.objects.create(**level)
            pereval = PerevalAdded.objects.create(**validated_data,
                                                   # add_image=images,
                                                      author=author,
                                                   # coords=coords,
                                                   # level=level
                                                     )

            # if images:
            #     for image in images:
            #         per_image_name = image.pop('image_name')
            #         per_image = image.pop('image')
            #         Images.objects.create(pereval=pereval,
            #                               per_image_name=per_image_name,
            #                               per_image=per_image)

        return pereval
