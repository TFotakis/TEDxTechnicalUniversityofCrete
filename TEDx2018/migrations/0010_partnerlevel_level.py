# Generated by Django 2.0.2 on 2018-03-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0009_auto_20180321_0332'),
	]

	operations = [
		migrations.AddField(
			model_name='partnerlevel',
			name='Level',
			field=models.IntegerField(blank=True, default=1),
		),
	]
