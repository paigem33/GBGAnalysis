# Generated by Django 3.2.25 on 2024-04-11 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GBGAnalysisApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('min_players', models.IntegerField(default=1)),
                ('max_players', models.IntegerField(default=1)),
                ('min_playtime', models.IntegerField(default=0)),
                ('max_playtime', models.IntegerField(default=0)),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
                ('description', models.CharField(max_length=20000)),
                ('publisher', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
    ]
