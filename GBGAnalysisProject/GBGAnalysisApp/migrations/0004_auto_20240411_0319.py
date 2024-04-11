# Generated by Django 3.2.25 on 2024-04-11 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GBGAnalysisApp', '0003_auto_20240411_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='age',
        ),
        migrations.RemoveField(
            model_name='review',
            name='description',
        ),
        migrations.RemoveField(
            model_name='review',
            name='max_players',
        ),
        migrations.RemoveField(
            model_name='review',
            name='max_playtime',
        ),
        migrations.RemoveField(
            model_name='review',
            name='min_players',
        ),
        migrations.RemoveField(
            model_name='review',
            name='min_playtime',
        ),
        migrations.RemoveField(
            model_name='review',
            name='publisher',
        ),
        migrations.AddField(
            model_name='gameboard',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='gameboard',
            name='description',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='gameboard',
            name='max_players',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='gameboard',
            name='max_playtime',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='gameboard',
            name='min_players',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='gameboard',
            name='min_playtime',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='gameboard',
            name='publisher',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]