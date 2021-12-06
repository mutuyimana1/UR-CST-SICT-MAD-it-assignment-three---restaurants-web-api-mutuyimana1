from django.contrib.auth.models import User
from django.db import models


class Dishes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='dishez')
    name = models.CharField(max_length=30)
    cookingTime = models.TimeField(blank=True, null=True, auto_now_add=True)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=255, null=True, blank=True)


    def __str__(self):
        return f"{self.name}  {self.price}Rwf  {self.image}"


class Restaurants(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=20)
    ownership = models.CharField(max_length=15, choices=[('INDIVIDUAL', 'Individual'), ('COMPANY', 'Company')])
    owner_name = models.CharField(max_length=30)
    rating = models.CharField(max_length=20,
                              choices=[('1STAR', '1star'), ('2STAR', '2star'), ('3STAR', '3star'), ('4STAR', '4star'),
                                       ('5STAR', '5star')])
    dishes = models.ForeignKey(Dishes, on_delete=models.PROTECT, related_name="Serves")
    district = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.owner_name} {self.district} {self.sector} {self.dishes.name}"
