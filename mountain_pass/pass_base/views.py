from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
