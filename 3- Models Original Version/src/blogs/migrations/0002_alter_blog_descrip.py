# Generated by Django 4.1.1 on 2022-09-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descrip',
            field=models.TextField(blank=True),
        ),
    ]