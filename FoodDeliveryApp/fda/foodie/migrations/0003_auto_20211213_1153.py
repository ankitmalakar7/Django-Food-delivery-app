# Generated by Django 3.2.9 on 2021-12-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
