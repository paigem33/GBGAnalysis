# Generated by Django 3.2.25 on 2024-04-11 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GBGAnalysisApp', '0005_auto_20240411_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameboard',
            name='category',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
