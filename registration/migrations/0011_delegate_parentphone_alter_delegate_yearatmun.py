# Generated by Django 4.0 on 2024-03-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_rename_streedaddr_delegate_streetaddr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegate',
            name='parentPhone',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delegate',
            name='yearAtMun',
            field=models.SmallIntegerField(null=True),
        ),
    ]