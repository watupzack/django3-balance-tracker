# Generated by Django 3.0.7 on 2020-06-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20200616_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbalance',
            name='ron',
            field=models.IntegerField(default=0),
        ),
    ]
