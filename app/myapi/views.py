from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('username')
    serializer_class = HeroSerializer