# Generated by Django 4.0.2 on 2022-02-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_timestamp_orderupdate_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
