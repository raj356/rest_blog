# Generated by Django 3.1.4 on 2020-12-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201221_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]