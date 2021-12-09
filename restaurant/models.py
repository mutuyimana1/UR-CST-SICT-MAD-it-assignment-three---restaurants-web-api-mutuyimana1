from django.contrib.auth.models import User
from django.db import models


class District(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Dishes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=30)
    cookingTime = models.CharField(max_length=30, null=True, blank=True,
                                   choices=[('06:00AM - 9:00AM', '06:00AM - 9:00AM'),
                                            ('09:00AM - 11:00AM', '09:00AM - 11:00AM'),
                                            ('11:00AM - 01:00PM', '11:00AM - 01:00PM'),
                                            ('01:00PM - 03:00PM', '01:00PM - 03:00PM'),
                                            ('03:00 AM - 05:00 PM', '03:00 AM - 05:00 PM'),
                                            ('05:00 PM - 07:00 PM', '05:00 PM - 07:00 PM'),
                                            ('07:00 PM - 08:00 PM', '07:00 PM - 08:00 PM')])
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/images/%Y/%m/%d/', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self):
        return f"{self.name}  {self.price}Rwf  {self.image}"


class Restaurants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=20)
    ownership = models.CharField(max_length=15, choices=[('INDIVIDUAL', 'Individual'), ('COMPANY', 'Company')])
    owner_name = models.CharField(max_length=30)
    rating = models.CharField(max_length=20,
                              choices=[('I STAR', 'I star'), ('II STAR', 'II star'), ('III STAR', 'III star'), ('IV STAR', 'IV star'),
                                       ('V STAR', 'V star')])
    dishes = models.ForeignKey(Dishes, on_delete=models.PROTECT, related_name="Serves")
    district = models.CharField(max_length=20, null=True, blank=True)
    sector = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()

    class Meta:
        verbose_name_plural = "restaurants"

    def __str__(self):
        return f"{self.name} {self.owner_name} {self.district} {self.sector} {self.dishes.name}"
