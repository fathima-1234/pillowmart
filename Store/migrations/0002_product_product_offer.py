# Generated by Django 4.2 on 2023-05-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_offer',
            field=models.IntegerField(default=0),
        ),
    ]
