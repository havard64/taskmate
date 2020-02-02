# Generated by Django 2.2.5 on 2020-01-27 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_diary_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='id',
        ),
        migrations.AddField(
            model_name='diary',
            name='date',
            field=models.DateField(default=datetime.date.today, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='diary',
            name='goal',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='diary',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
