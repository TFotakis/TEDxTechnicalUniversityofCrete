# Generated by Django 2.0.4 on 2018-05-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0034_event_ticketsnumber'),
	]

	operations = [
		migrations.AlterField(
			model_name='event',
			name='TicketsNumber',
			field=models.IntegerField(blank=True, default=0),
		),
	]