# Generated by Django 2.0.2 on 2018-03-27 02:25

from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0024_event_scheduleannounced'),
	]

	operations = [
		migrations.RenameField(
			model_name='event',
			old_name='Location',
			new_name='Address1',
		),
	]
