from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Restaurant, Menu, Employee, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer

class RestaurantModelTest(TestCase):
    def test_str_representation(self):
        restaurant = Restaurant(name='Restaurant A', address='123 Main Street')
        self.assertEqual(str(restaurant), 'Restaurant A')

class MenuModelTest(TestCase):
    def test_str_representation(self):
        restaurant = Restaurant(name='Restaurant A', address='123 Main Street')
        menu = Menu(restaurant=restaurant, date='2023-07-15', menu_items='Menu items')
        self.assertEqual(str(menu), 'Restaurant A - 2023-07-15')

class EmployeeModelTest(TestCase):
    def test_str_representation(self):
        employee = Employee(name='John Doe', email='john@example.com')
        self.assertEqual(str(employee), 'John Doe')

class VoteModelTest(TestCase):
    def test_str_representation(self):
        restaurant = Restaurant(name='Restaurant A', address='123 Main Street')
        menu = Menu(restaurant=restaurant, date='2023-07-15', menu_items='Menu items')
        employee = Employee(name='John Doe', email='john@example.com')
        vote = Vote(employee=employee, menu=menu, vote_value=1)
        self.assertEqual(str(vote), 'John Doe - Restaurant A - 2023-07-15')
