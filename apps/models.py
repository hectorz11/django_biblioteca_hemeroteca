# -*- encoding: utf-8 -*-
from django.db import models

class Classification(models.Model):
	name = models.CharField(max_length=100, verbose_name='Clasificación')
	status = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['id']
		verbose_name_plural = 'Clasificaciones'

class Location(models.Model):
	name = models.CharField(max_length=100, verbose_name='Ubicación')
	status = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['id']
		verbose_name_plural = 'Ubicaciones'

class State(models.Model):
	name = models.CharField(max_length=100, verbose_name='Estado')
	status = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['id']
		verbose_name_plural = 'Estados'

class Type(models.Model):
	name = models.CharField(max_length=100, verbose_name='Tipo')
	status = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['id']
		verbose_name_plural = 'Tipos'

class Book(models.Model):
	code = models.CharField(max_length=50, blank=True, null=True, verbose_name='Código')
	authors = models.CharField(max_length=250, blank=True, null=True, verbose_name='Autor(es)')
	title = models.CharField(max_length=250, verbose_name='Título')
	edition = models.CharField(max_length=250, blank=True, null=True, verbose_name='Edición')
	year = models.CharField(max_length=10, blank=True, null=True, verbose_name='Año')
	content = models.TextField(max_length=1500, blank=True, null=True, verbose_name='Contenido')
	classification = models.ForeignKey(Classification, verbose_name='Clasificación')
	location = models.ForeignKey(Location, verbose_name='Ubicación')
	state = models.ForeignKey(State, verbose_name='Estado')
	description = models.TextField(max_length=1500, blank=True, null=True, verbose_name='Descripción')
	observation = models.TextField(max_length=1500, blank=True, null=True, verbose_name='Observaciones')
	status = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['id']
		verbose_name_plural = 'Biblioteca'

class Newspaper(models.Model):
	volume = models.CharField(max_length=50, blank=True, null=True, verbose_name='Volumen')
	name = models.CharField(max_length=250, verbose_name='Nombre')
	date_start = models.CharField(max_length=25, blank=True, null=True, verbose_name='Fecha de inicio')
	date_end = models.CharField(max_length=25, blank=True, null=True, verbose_name='Fecha de finalización')
	classification = models.ForeignKey(Classification, verbose_name='Clasificación')
	location = models.ForeignKey(Location, verbose_name='Ubicación')
	state = models.ForeignKey(State, verbose_name='Estado')
	types = models.ForeignKey(Type, verbose_name='Tipo')
	description = models.TextField(max_length=1500, blank=True, null=True, verbose_name='Descripción')
	observation = models.TextField(max_length=1500, blank=True, null=True, verbose_name='Observaciones')
	status = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['id']
		verbose_name_plural = 'Hemeroteca'