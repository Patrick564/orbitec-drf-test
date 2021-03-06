# Generated by Django 4.0.4 on 2022-05-19 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('alias', models.CharField(max_length=10)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('company', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(default='(No specified)', max_length=250)),
                ('gps_id', models.CharField(default='(No specified)', max_length=150)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
