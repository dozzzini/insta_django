# Generated by Django 4.2.3 on 2023-07-25 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followingNum',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
