# Generated by Django 2.0.6 on 2018-07-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfcutter', '0016_auto_20180705_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
