from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from restaurant import views

router = routers.SimpleRouter()
router.register(r"dishes", views.DishesModelViewSet, basename="dish")
router.register(r"restaurant", views.RestaurantModelViewSet, basename="restaurant")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),

]
