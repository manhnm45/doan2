# Generated by Django 5.0 on 2023-12-22 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='weith',
            fields=[
                ('weight_id', models.AutoField(primary_key=True, serialize=False)),
                ('unit_weight', models.IntegerField(null=True)),
                ('weight_current', models.IntegerField(null=True)),
                ('number', models.IntegerField(null=True)),
                ('scale_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.demoscale')),
            ],
        ),
    ]
