# Generated by Django 4.0 on 2024-03-23 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='country',
            name='numAllowed',
            field=models.SmallIntegerField(default=1),
        ),
    ]
