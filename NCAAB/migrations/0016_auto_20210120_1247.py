# Generated by Django 3.1.5 on 2021-01-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NCAAB', '0015_auto_20210120_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='text',
            new_name='full_text',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
