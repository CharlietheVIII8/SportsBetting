# Generated by Django 3.1.5 on 2021-01-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NCAAB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='home_losses',
            field=models.IntegerField(null=True),
        ),
    ]
