# Generated by Django 3.2.9 on 2021-12-08 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dishes',
            options={'verbose_name_plural': 'dishes'},
        ),
        migrations.AlterModelOptions(
            name='restaurants',
            options={'verbose_name_plural': 'restaurants'},
        ),
        migrations.AddField(
            model_name='dishes',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='static/images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurants',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dishes',
            name='cookingTime',
            field=models.CharField(blank=True, choices=[('06:00AM - 9:00AM', '06:00AM - 9:00AM'), ('09:00AM - 11:00AM', '09:00AM - 11:00AM'), ('11:00AM - 01:00PM', '11:00AM - 01:00PM'), ('01:00PM - 03:00PM', '01:00PM - 03:00PM'), ('03:00 AM - 05:00 PM', '03:00 AM - 05:00 PM'), ('05:00 PM - 07:00 PM', '05:00 PM - 07:00 PM'), ('07:00 PM - 08:00 PM', '07:00 PM - 08:00 PM')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='district',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='ownership',
            field=models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('COMPANY', 'Company')], max_length=15),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='rating',
            field=models.CharField(choices=[('I STAR', 'I star'), ('II STAR', 'II star'), ('III STAR', 'III star'), ('IV STAR', 'IV star'), ('V STAR', 'V star')], max_length=20),
        ),
    ]