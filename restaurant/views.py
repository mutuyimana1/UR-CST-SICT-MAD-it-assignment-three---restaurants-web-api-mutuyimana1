from django.http import HttpResponse
from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Dishes, Restaurants
# from restaurant.permit import IsAdminUserOrReadOnly
from restaurant.serializer import DishesSerializer, WriteRestaurantsSerializer, ReadRestaurantsSerializer


def home(request):
    return render(request, 'index.html')


class DishesModelViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = DishesSerializer
    pagination_class = None

    def get_queryset(self):
        return Dishes.objects.filter(user=self.request.user)


class RestaurantModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("district", "sector",)
    filterset_fields = ("dishes__name",)

    def get_queryset(self):
        return Restaurants.objects.select_related("dishes", "user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadRestaurantsSerializer
        return WriteRestaurantsSerializer

    @api_view(['GET', 'PUT', 'DELETE'])
    def rest_detail(request, pk):
        try:
            resto = Restaurants.objects.get(location=pk)

        except Restaurants.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ReadRestaurantsSerializer(resto)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ReadRestaurantsSerializer(resto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            resto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
