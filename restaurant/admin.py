from django.contrib import admin

from restaurant.models import Dishes, Restaurants

admin.site.register(Dishes),
admin.site.register(Restaurants)