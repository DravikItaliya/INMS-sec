# Generated by Django 3.2.13 on 2022-05-11 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cat_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='token',
        ),
        migrations.RemoveField(
            model_name='face',
            name='supervisor',
        ),
    ]
