from django.contrib import admin

from restaurant.models import Dishes, Restaurants, District

admin.site.register(Dishes),
admin.site.register(Restaurants),
admin.site.register(District)