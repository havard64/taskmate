# Generated by Django 2.2.5 on 2020-02-12 18:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.TextField(blank=True, default='', null=True)),
                ('notes', models.TextField(blank=True, default='', null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('feelgood', models.CharField(default='Fantastic', max_length=30, null=True)),
                ('productivity', models.CharField(default='Fantastic', max_length=30, null=True)),
                ('metime', models.CharField(default='Fantastic', max_length=30, null=True)),
                ('fftime', models.CharField(default='Fantastic', max_length=30, null=True)),
                ('manage', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('manage', 'date')},
            },
        ),
    ]
