# Generated by Django 3.2.13 on 2022-05-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_save_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='cat',
            field=models.CharField(max_length=50),
        ),
    ]