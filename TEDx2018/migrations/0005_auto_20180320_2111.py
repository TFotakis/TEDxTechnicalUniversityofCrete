# Generated by Django 2.0.2 on 2018-03-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0004_auto_20180320_1650'),
	]

	operations = [
		migrations.AddField(
			model_name='speaker',
			name='Title',
			field=models.CharField(blank=True, max_length=100),
		),
		migrations.AlterField(
			model_name='event',
			name='EventImage',
			field=models.ImageField(blank=True, default='TEDx2018/Shared/XBlackBig.svg', upload_to='TEDx2018/EventPictures/'),
		),
		migrations.AlterField(
			model_name='partner',
			name='Logo',
			field=models.ImageField(blank=True, default='TEDx2018/Shared/XWhite.svg', upload_to='TEDx2018/SponsorLogos/'),
		),
		migrations.AlterField(
			model_name='speaker',
			name='ProfileImage',
			field=models.ImageField(blank=True, default='TEDx2018/Shared/XWhite.svg', upload_to='TEDx2018/SpeakerProfilePictures/'),
		),
		migrations.AlterField(
			model_name='teammember',
			name='ProfileImage',
			field=models.ImageField(blank=True, default='TEDx2018/Shared/XWhite.svg', upload_to='TEDx2018/TeamMemberProfilePictures/'),
		),
	]
