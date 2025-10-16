from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField()
    colour=models.CharField(max_length=100)
class CarAdmin(admin.ModelAdmin):
    list_display=('car_id','brand','model', 'year','price','colour')
