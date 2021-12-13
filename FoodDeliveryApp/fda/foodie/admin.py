from django.contrib import admin

# Register your models here.
from .models import Foods, Order

admin.site.register(Foods)
admin.site.register(Order)
