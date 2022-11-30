from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Poorvika
# from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .serializers import *


class poorvika_price_filter(generics.ListAPIView):
    queryset=Poorvika.objects.all()
    serializer_class = poorvika_serializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date','category','brand']

class poorvika_price(generics.ListAPIView):
    queryset=Poorvika.objects.all()
    serializer_class = poorvika_serializer

class home_appliance(generics.ListAPIView):
    queryset= HomeApplainces.objects.all()
    serializer_class = home_appliance_serializer
