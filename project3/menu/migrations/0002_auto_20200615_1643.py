# Generated by Django 3.0.7 on 2020-06-15 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pizzamenuitem',
            unique_together={('pizza_type', 'toppings')},
        ),
    ]
