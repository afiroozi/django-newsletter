# Generated by Django 2.0 on 2018-02-28 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]
