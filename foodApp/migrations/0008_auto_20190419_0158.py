# Generated by Django 2.2 on 2019-04-18 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0007_remove_donatedfood_donator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donatedfood',
            name='volunter',
            field=models.ForeignKey(limit_choices_to={'volunter': 'Y'}, on_delete=django.db.models.deletion.CASCADE, to='foodApp.Profile'),
        ),
    ]