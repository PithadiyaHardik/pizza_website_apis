# Generated by Django 3.2.6 on 2021-08-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(max_length=20)),
                ('pizza_size', models.CharField(max_length=20)),
                ('pizza_topping', models.CharField(max_length=20)),
            ],
        ),
    ]