# Generated by Django 4.2.9 on 2024-01-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ticker',
            field=models.CharField(default='NULL', max_length=4),
        ),
    ]
