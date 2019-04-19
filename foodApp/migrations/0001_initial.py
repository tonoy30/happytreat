# Generated by Django 2.2 on 2019-04-19 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14, unique=True)),
                ('address', models.TextField()),
                ('volunter', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=1)),
                ('avaliable', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('expire_time', models.PositiveSmallIntegerField(default=0)),
                ('food_desc', models.TextField()),
                ('pick_up_time', models.TimeField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('food_status', models.CharField(choices=[('REQ', 'REQ'), ('PRO', 'PRO'), ('REC', 'REC')], default='REQ', max_length=3)),
                ('donator', models.ForeignKey(limit_choices_to={'volunter': 'N'}, on_delete=django.db.models.deletion.CASCADE, to='foodApp.Profile')),
            ],
            options={
                'ordering': ('-date_time', 'food_status'),
            },
        ),
        migrations.CreateModel(
            name='DonatedFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donated_area', models.CharField(max_length=100)),
                ('beneficent', models.PositiveSmallIntegerField(default=0)),
                ('finished', models.DateTimeField(auto_now=True)),
                ('donated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodApp.FoodRequest')),
                ('volunter', models.ForeignKey(limit_choices_to={'volunter': 'Y'}, on_delete=django.db.models.deletion.CASCADE, to='foodApp.Profile')),
            ],
            options={
                'ordering': ('-finished',),
            },
        ),
    ]
