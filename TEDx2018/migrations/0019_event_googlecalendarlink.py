# Generated by Django 2.0.2 on 2018-03-24 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0018_auto_20180324_0250'),
	]

	operations = [
		migrations.AddField(
			model_name='event',
			name='GoogleCalendarLink',
			field=models.TextField(blank=True),
		),
	]
