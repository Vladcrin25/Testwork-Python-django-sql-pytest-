from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Restaurant, Menu, Employee, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer
from django.utils import timezone
from django.shortcuts import render

class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CurrentDayMenuView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        current_date = timezone.now().date()
        return Menu.objects.filter(date=current_date)

class CurrentDayResultsView(generics.ListAPIView):
    serializer_class = VoteSerializer

    def get_queryset(self):
        current_date = timezone.now().date()
        return Vote.objects.filter(menu__date=current_date)
