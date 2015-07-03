# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=50, null=True, verbose_name=b'C\xc3\xb3digo', blank=True)),
                ('authors', models.CharField(max_length=250, null=True, verbose_name=b'Autor(es)', blank=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'T\xc3\xadtulo')),
                ('edition', models.CharField(max_length=250, null=True, verbose_name=b'Edici\xc3\xb3n', blank=True)),
                ('year', models.CharField(max_length=10, null=True, verbose_name=b'A\xc3\xb1o', blank=True)),
                ('content', models.TextField(max_length=1500, null=True, verbose_name=b'Contenido', blank=True)),
                ('description', models.TextField(max_length=1500, null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('observation', models.TextField(max_length=1500, null=True, verbose_name=b'Observaciones', blank=True)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Biblioteca',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Clasificaci\xc3\xb3n')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Clasificaciones',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Ubicaci\xc3\xb3n')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Ubicaciones',
            },
        ),
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.CharField(max_length=50, null=True, verbose_name=b'Volumen', blank=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Nombre')),
                ('date_start', models.CharField(max_length=25, null=True, verbose_name=b'Fecha de inicio', blank=True)),
                ('date_end', models.CharField(max_length=25, null=True, verbose_name=b'Fecha de finalizaci\xc3\xb3n', blank=True)),
                ('description', models.TextField(max_length=1500, null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('observation', models.TextField(max_length=1500, null=True, verbose_name=b'Observaciones', blank=True)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('classification', models.ForeignKey(verbose_name=b'Clasificaci\xc3\xb3n', to='apps.Classification')),
                ('location', models.ForeignKey(verbose_name=b'Ubicaci\xc3\xb3n', to='apps.Location')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Hemeroteca',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Estado')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Tipo')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.AddField(
            model_name='newspaper',
            name='state',
            field=models.ForeignKey(verbose_name=b'Estado', to='apps.State'),
        ),
        migrations.AddField(
            model_name='newspaper',
            name='types',
            field=models.ForeignKey(verbose_name=b'Tipo', to='apps.Type'),
        ),
        migrations.AddField(
            model_name='book',
            name='classification',
            field=models.ForeignKey(verbose_name=b'Clasificaci\xc3\xb3n', to='apps.Classification'),
        ),
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.ForeignKey(verbose_name=b'Ubicaci\xc3\xb3n', to='apps.Location'),
        ),
        migrations.AddField(
            model_name='book',
            name='state',
            field=models.ForeignKey(verbose_name=b'Estado', to='apps.State'),
        ),
    ]
