# Generated by Django 4.0.2 on 2022-02-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0002_city_dayweek_speciality_state_profile_favorites_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
