# Generated by Django 3.1.5 on 2021-01-19 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NCAAB', '0008_auto_20210118_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameboxscore',
            name='winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='boxscore_winner', to='NCAAB.team'),
        ),
        migrations.AlterUniqueTogether(
            name='gameboxscore',
            unique_together={('date', 'winner', 'loser')},
        ),
    ]