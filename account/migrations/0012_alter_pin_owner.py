# Generated by Django 3.2.6 on 2021-10-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20211006_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='owner',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
