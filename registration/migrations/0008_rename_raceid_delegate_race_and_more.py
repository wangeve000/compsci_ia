# Generated by Django 4.0 on 2024-03-26 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_delegate_schoolid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delegate',
            old_name='raceId',
            new_name='race',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='stateId',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='delegation',
            old_name='assignedCountryID',
            new_name='assignedCountry',
        ),
        migrations.RenameField(
            model_name='delegation',
            old_name='schoolId',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='delegation',
            old_name='teamId',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='registry',
            old_name='countryId',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='registry',
            old_name='teamId',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='delegateId1',
            new_name='delegate1',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='delegateId2',
            new_name='delegate2',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='delegateId3',
            new_name='delegate3',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='delegateId4',
            new_name='delegate4',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='schoolId',
            new_name='school',
        ),
    ]
