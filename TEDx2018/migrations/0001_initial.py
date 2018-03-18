# Generated by Django 2.0.2 on 2018-03-09 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Event',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('Name', models.CharField(max_length=100)),
				('Location', models.CharField(blank=True, max_length=200)),
				('GoogleMapsLink', models.CharField(blank=True, max_length=200)),
				('StartDateTime', models.DateTimeField(blank=True, default=None, null=True)),
				('EndDateTime', models.DateTimeField(blank=True, default=None, null=True)),
				('EventImage', models.ImageField(blank=True, upload_to='EventPictures/')),
				('EventDescription', models.TextField(blank=True)),
				('TicketsNumber', models.IntegerField(blank=True, default=0)),
				('SoldOut', models.BooleanField(default=False)),
				('Eventbrite', models.CharField(blank=True, max_length=100)),
				('Facebook', models.CharField(blank=True, max_length=100)),
				('GitHub', models.CharField(blank=True, max_length=100)),
				('GooglePlus', models.CharField(blank=True, max_length=100)),
				('Instagram', models.CharField(blank=True, max_length=100)),
				('LinkedIn', models.CharField(blank=True, max_length=100)),
				('Pinterest', models.CharField(blank=True, max_length=100)),
				('Twitter', models.CharField(blank=True, max_length=100)),
				('YouTube', models.CharField(blank=True, max_length=100)),
			],
		),
		migrations.CreateModel(
			name='Partner',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('CompanyName', models.CharField(max_length=100)),
				('Name', models.CharField(blank=True, max_length=100)),
				('Surname', models.CharField(blank=True, max_length=100)),
				('email', models.CharField(blank=True, max_length=100)),
				('Telephone', models.IntegerField(blank=True, null=True)),
				('Logo', models.ImageField(blank=True, default='TEDx2018/Shared/defaultSponsorLogo.png', upload_to='TEDx2018/SponsorLogos/')),
				('AnnouncementDateTime', models.DateTimeField(blank=True, default=None, null=True)),
				('Announced', models.BooleanField(default=False)),
				('InternetLink', models.CharField(blank=True, max_length=100)),
				('Event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event')),
			],
		),
		migrations.CreateModel(
			name='PartnerLevel',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('Name', models.CharField(max_length=100)),
				('Event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event')),
			],
		),
		migrations.CreateModel(
			name='Position',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('Name', models.CharField(max_length=100)),
				('Event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event')),
			],
		),
		migrations.CreateModel(
			name='Speaker',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('Name', models.CharField(max_length=100)),
				('Surname', models.CharField(max_length=100)),
				('email', models.CharField(blank=True, max_length=100)),
				('Telephone', models.IntegerField(blank=True, null=True)),
				('ProfileImage', models.ImageField(blank=True, default='TEDx2018/Shared/defaultProfile.png', upload_to='TEDx2018/SpeakerProfilePictures/')),
				('Bio', models.TextField(blank=True)),
				('AnnouncementDateTime', models.DateTimeField(blank=True, default=None, null=True)),
				('Announced', models.BooleanField(default=False)),
				('Presentation', models.FileField(blank=True, upload_to='TEDx2018/SpeakerPresentations/')),
				('PresentationReleaseDateTime', models.DateTimeField(blank=True, default=None, null=True)),
				('PresentationRelease', models.BooleanField(default=False)),
				('Facebook', models.CharField(blank=True, max_length=100)),
				('GitHub', models.CharField(blank=True, max_length=100)),
				('GooglePlus', models.CharField(blank=True, max_length=100)),
				('Instagram', models.CharField(blank=True, max_length=100)),
				('LinkedIn', models.CharField(blank=True, max_length=100)),
				('Pinterest', models.CharField(blank=True, max_length=100)),
				('Twitter', models.CharField(blank=True, max_length=100)),
				('YouTube', models.CharField(blank=True, max_length=100)),
				('InternetLink', models.CharField(blank=True, max_length=100)),
				('Event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event')),
			],
		),
		migrations.CreateModel(
			name='Team',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('Name', models.CharField(max_length=100)),
				('Event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event')),
			],
		),
		migrations.CreateModel(
			name='TeamMember',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('Name', models.CharField(max_length=100)),
				('Surname', models.CharField(max_length=100)),
				('email', models.CharField(max_length=100)),
				('Telephone', models.IntegerField()),
				('University', models.CharField(max_length=100)),
				('School', models.CharField(max_length=100)),
				('EducationalLevel', models.CharField(max_length=100)),
				('ProfileImage', models.ImageField(blank=True, default='TEDx2018/Shared/defaultProfile.png', upload_to='TEDx2018/TeamMemberProfilePictures/')),
				('Bio', models.TextField(blank=True)),
				('Facebook', models.CharField(blank=True, max_length=100)),
				('GitHub', models.CharField(blank=True, max_length=100)),
				('GooglePlus', models.CharField(blank=True, max_length=100)),
				('Instagram', models.CharField(blank=True, max_length=100)),
				('LinkedIn', models.CharField(blank=True, max_length=100)),
				('Pinterest', models.CharField(blank=True, max_length=100)),
				('Twitter', models.CharField(blank=True, max_length=100)),
				('YouTube', models.CharField(blank=True, max_length=100)),
				('Event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event')),
				('Position', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='TEDx2018.Position')),
			],
		),
		migrations.CreateModel(
			name='TeamMemberAssignment',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('Event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event')),
				('Team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Team')),
				('TeamMember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.TeamMember')),
			],
		),
		migrations.CreateModel(
			name='Ticket',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('Name', models.CharField(max_length=100)),
				('Price', models.FloatField(default=0)),
				('Quantity', models.IntegerField(default=0)),
				('Event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event')),
			],
		),
		migrations.AddField(
			model_name='partner',
			name='PartnerLevel',
			field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.PartnerLevel'),
		),
	]