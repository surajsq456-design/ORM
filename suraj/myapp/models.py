from django.db import models
from django.contrib import admin

class product(models.Model):
    product_name=models.CharField(max_length=100)
    product_id=models.IntegerField(primary_key=True)
    manufacture_date=models.DateField()
    transport_details=models.CharField(max_length=20)
    product_quantity=models.IntegerField()
    price=models.IntegerField()

class amazon_admin(admin.ModelAdmin):
    list_display=["product_name","product_id","manufacture_date","transport_details","product_quantity","price"]
