# Generated by Django 2.2.11 on 2020-03-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='flag_computed',
        ),
        migrations.AddField(
            model_name='moviesvotes',
            name='date_vote',
            field=models.DateTimeField(auto_now=True, verbose_name='Date'),
        ),
    ]
