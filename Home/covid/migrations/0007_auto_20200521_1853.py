# Generated by Django 3.0.3 on 2020-05-21 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0006_auto_20200518_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='LargeData',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('fever', models.IntegerField()),
                ('cough', models.IntegerField()),
                ('throat', models.IntegerField()),
                ('weakness', models.IntegerField()),
                ('diffBreath', models.IntegerField()),
                ('drowsiness', models.IntegerField()),
                ('pain', models.IntegerField()),
                ('travel', models.IntegerField()),
                ('symptoms', models.IntegerField()),
                ('blood', models.IntegerField()),
                ('appetide', models.IntegerField()),
                ('result', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userdata',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
