# Generated by Django 2.0.2 on 2018-03-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0026_event_address2'),
	]

	operations = [
		migrations.AddField(
			model_name='event',
			name='HasAnnouncedSpeakers',
			field=models.BooleanField(default=False),
		),
	]
