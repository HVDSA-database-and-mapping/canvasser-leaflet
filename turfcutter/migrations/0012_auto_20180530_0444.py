# Generated by Django 2.0.5 on 2018-05-30 04:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfcutter', '0011_auto_20180530_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='accepted_material',
            field=models.BooleanField(choices=[(True, '✅'), (False, '❌')], default=False),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='at_home',
            field=models.BooleanField(choices=[(True, '✅'), (False, '❌')], default=False),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='campaign_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='campaign_response',
            field=models.SmallIntegerField(choices=[(1, '😠'), (2, '😐'), (3, '😍')], default=2),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='dsa_response',
            field=models.SmallIntegerField(choices=[(1, '😠'), (2, '😐'), (3, '😍')], default=2),
        ),
    ]
