from django.contrib.auth.models import User
from rest_framework import serializers

from restaurant.models import Dishes, Restaurants


class DishesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Dishes
        fields = ("id", "name", "cookingTime", "ingredients", "price", "user", "image")


class WriteRestaurantsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    dishes = serializers.SlugRelatedField(slug_field="name", queryset=Dishes.objects.all())


    class Meta:
        model = Restaurants
        fields = (
            "user", "name", "ownership", "owner_name", "rating", "dishes", "district", "sector", "address", "contact")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            user = self.context["request"].user
            self.fields["dishes"].queryset = user.dishes.all()


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")
        read_only_fields = fields


class ReadRestaurantsSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()
    dishes = DishesSerializer()

    class Meta:
        model = Restaurants
        fields = (
            "id",
            "name",
            "ownership",
            "owner_name",
            "rating",
            "dishes",
            "district",
            "sector",
            "address",
            "contact",
            "user",
        )
        read_only_fields = fields
