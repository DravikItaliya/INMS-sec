# Generated by Django 3.2.13 on 2022-05-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_lastface'),
    ]

    operations = [
        migrations.CreateModel(
            name='cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='super',
        ),
    ]
