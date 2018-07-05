# Generated by Django 2.0.6 on 2018-07-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfcutter', '0015_auto_20180705_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='countyname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='firstname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='gender',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='housenumchar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='housesuffix',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='isnthaddress',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='jurisdname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='lastname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='mailaddress1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='mailaddress2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='mailaddress3',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='mailaddress4',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='mailaddress5',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='middlename',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='munidcode',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='nthdescription',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='permavind',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='pocity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='postate',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='predirection',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='probatecdcode',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='resext',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='schoolname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='statustype',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='streetname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='streettype',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='sufdirection',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='suffix',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='villagename',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='villageprecinct',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voted',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='votedav',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voterid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]