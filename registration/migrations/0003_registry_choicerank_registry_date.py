# Generated by Django 4.0 on 2024-03-23 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('registration', '0002_country_numallowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='registry',
            name='choiceRank',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='registry',
            name='registry_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 23, 3, 21, 20, 240327), editable=False),
        ),
    ]
