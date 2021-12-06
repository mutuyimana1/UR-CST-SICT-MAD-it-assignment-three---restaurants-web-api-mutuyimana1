from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from restaurant import views

router = routers.SimpleRouter()
router.register(r"dishes", views.DishesModelViewSet, basename="dish")
router.register(r"restaurant", views.RestaurantModelViewSet, basename="restaurant")
urlpatterns = [
                  path('api-auth/', include('rest_framework.urls')),
                  path('login/', obtain_auth_token, name="obtain_auth_token"),
                  path('admin/', admin.site.urls),

              ] + router.urls
