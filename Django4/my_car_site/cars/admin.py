from django.contrib import admin
from cars.models import Car

# admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TIME INFORMATION', {'fields':['year']}),
        ('CAR INFORMATION', {'fields':['brand']})
    ]

admin.site.register(Car, CarAdmin)