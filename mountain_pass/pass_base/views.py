from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import *


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class PerevalImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class SubmitData(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalAddedSerializer
    http_method_names = ['get', 'post', 'head', 'patch', 'options']

    def create(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({f'status': status.HTTP_201_CREATED,
                             'message': 'Запись успешно создана',
                             'id': obj.id})
        if status.HTTP_400_BAD_REQUEST:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'message': serializer.errors})
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                             'message': serializer.errors})

