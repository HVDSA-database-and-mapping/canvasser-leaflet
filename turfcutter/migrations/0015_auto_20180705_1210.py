# Generated by Django 2.0.6 on 2018-07-05 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turfcutter', '0014_election'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Election',
            new_name='Voter',
        ),
    ]
