# Generated by Django 2.2 on 2019-04-18 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


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
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodRequest',
            fields=[
                ('food_id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('expire_time', models.PositiveSmallIntegerField(default=0)),
                ('food_desc', models.TextField()),
                ('pick_up_time', models.TimeField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('food_status', models.CharField(choices=[('REQ', 'REQ'), ('PRO', 'PRO'), ('REC', 'REC')], default='REQ', max_length=3)),
                ('donator', models.ForeignKey(limit_choices_to={'is_volunter': False}, on_delete=django.db.models.deletion.CASCADE, to='foodApp.Profile')),
            ],
            options={
                'ordering': ('-date_time', 'food_status'),
            },
        ),
    ]