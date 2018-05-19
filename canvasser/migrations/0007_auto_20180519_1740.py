# Generated by Django 2.0.4 on 2018-05-19 17:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canvasser', '0006_canvas_campaign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('canvas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canvasser.Canvas')),
                ('canvassers', models.ManyToManyField(to='canvasser.Canvasser')),
            ],
        ),
        migrations.RemoveField(
            model_name='canvassector',
            name='canvas',
        ),
        migrations.RemoveField(
            model_name='canvassector',
            name='canvassers',
        ),
        migrations.RemoveField(
            model_name='canvasarea',
            name='id',
        ),
        migrations.AlterField(
            model_name='canvasarea',
            name='canvas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='canvasser.Canvas'),
        ),
        migrations.DeleteModel(
            name='CanvasSector',
        ),
    ]
