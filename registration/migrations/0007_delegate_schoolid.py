# Generated by Django 4.0 on 2024-03-26 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_alter_delegation_assignedcountryid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegate',
            name='schoolId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registration.school'),
            preserve_default=False,
        ),
    ]