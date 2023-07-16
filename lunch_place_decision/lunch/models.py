from django.db import models
from django.utils import timezone


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    menu_items = models.TextField()

    def __str__(self):
        return f"{self.restaurant.name} - {self.date}"

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Add more fields as needed

    def __str__(self):
        return self.name

class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    vote_value = models.IntegerField(choices=[(1, 'Positive'), (-1, 'Negative')])

    def __str__(self):
        return f"{self.employee.name} - {self.menu}"