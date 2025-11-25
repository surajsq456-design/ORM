# Ex01 Django ORM Web Application
## Date: 25.11.25

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM

from django.db import models
from django.contrib import admin
class Car(models.Model):
    brand_name = models.CharField()
    car_name = models.CharField()
    enginenum = models.IntegerField()
    release_date = models.DateField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand_name','car_name','enginenum','release_date')

from django.contrib import admin
from.models import Car,CarAdmin
admin.site.register(Car,CarAdmin)



## OUTPUT

![alt text](<Screenshot 2025-11-25 210111.png>)
![alt text](<Screenshot 2025-11-25 210659.png>)

## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
