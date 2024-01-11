from django.shortcuts import render
from .serializers import ItemSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from .models import Item

# Create your views here.
class Home(ListAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    