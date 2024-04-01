# Generated by Django 4.0 on 2024-03-26 00:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_school_alter_registry_registry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegation',
            name='delegateId1',
        ),
        migrations.RemoveField(
            model_name='delegation',
            name='delegateId2',
        ),
        migrations.RemoveField(
            model_name='delegation',
            name='delegateId3',
        ),
        migrations.RemoveField(
            model_name='delegation',
            name='delegateId4',
        ),
        migrations.RemoveField(
            model_name='registry',
            name='delegationId',
        ),
        migrations.RemoveField(
            model_name='registry',
            name='registry_date',
        ),
        migrations.AddField(
            model_name='delegate',
            name='role',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='delegation',
            name='assignedCountryID',
            field=models.ForeignKey(default=28, on_delete=django.db.models.deletion.CASCADE, to='registration.country'),
        ),
        migrations.AddField(
            model_name='delegation',
            name='schoolId',
            field=models.ForeignKey(default=43, on_delete=django.db.models.deletion.CASCADE, to='registration.school'),
        ),
        migrations.AddField(
            model_name='registry',
            name='registryTime',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 26, 0, 43, 4, 816003, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delegate',
            name='raceId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.race'),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='stateId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.state'),
        ),
        migrations.AlterField(
            model_name='registry',
            name='countryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.country'),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delegateId1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegate1', to='registration.delegate')),
                ('delegateId2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegate2', to='registration.delegate')),
                ('delegateId3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegate3', to='registration.delegate')),
                ('delegateId4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegate4', to='registration.delegate')),
                ('schoolId', models.ForeignKey(default=43, on_delete=django.db.models.deletion.CASCADE, to='registration.school')),
            ],
        ),
        migrations.AddField(
            model_name='delegation',
            name='teamId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registration.team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registry',
            name='teamId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registration.team'),
            preserve_default=False,
        ),
    ]