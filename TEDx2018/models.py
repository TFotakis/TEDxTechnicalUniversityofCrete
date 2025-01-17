from datetime import datetime

import requests
from bs4 import BeautifulSoup
from django.db import models


class Event(models.Model):
	Name = models.CharField(max_length=100)
	Address1 = models.CharField(max_length=200, blank=True)
	Address2 = models.CharField(max_length=200, blank=True)
	GoogleMapsLink = models.CharField(max_length=200, blank=True)
	GoogleCalendarLink = models.TextField(blank=True)
	StartDateTime = models.DateTimeField(default=None, blank=True, null=True)
	EndDateTime = models.DateTimeField(default=None, blank=True, null=True)
	IsOnGoing = models.BooleanField(default=False, blank=True)
	CarouselImage = models.ImageField(default='TEDx2018/Shared/XBlackBig.svg', blank=True, upload_to='TEDx2018/EventPictures/')
	Logo = models.ImageField(default='TEDx2018/Shared/XBlackBig.svg', blank=True, upload_to='TEDx2018/EventPictures/')
	AnnouncementDateTime = models.DateTimeField(default=None, blank=True, null=True)
	Description = models.TextField(blank=True)
	TicketsAvailable = models.BooleanField(default=False)
	TicketsNumber = models.IntegerField(blank=True, default=0)
	HasAnnouncedSpeakers = models.BooleanField(default=False)
	HasAnnouncedWorkshops = models.BooleanField(default=False)
	ScheduleAnnounced = models.BooleanField(default=False)
	Eventbrite = models.CharField(max_length=100, blank=True, default='#')
	Facebook = models.CharField(max_length=100, blank=True)
	GitHub = models.CharField(max_length=100, blank=True)
	GooglePlus = models.CharField(max_length=100, blank=True)
	Instagram = models.CharField(max_length=100, blank=True)
	LinkedIn = models.CharField(max_length=100, blank=True)
	Pinterest = models.CharField(max_length=100, blank=True)
	Reddit = models.CharField(max_length=100, blank=True)
	Twitter = models.CharField(max_length=100, blank=True)
	YouTube = models.CharField(max_length=100, blank=True)

	@property
	def Announced(self):
		return True if self.AnnouncementDateTime is None else self.AnnouncementDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple()

	@property
	def Past(self):
		return True if self.EndDateTime is None else self.EndDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple()

	@property
	def HasLinks(self):
		return bool(self.Facebook) | bool(self.GitHub) | bool(self.GooglePlus) | bool(self.Instagram) | bool(self.LinkedIn) | bool(self.Pinterest) | bool(self.Twitter) | bool(self.YouTube)

	@property
	def HasTalkLinks(self):
		return self.speaker_set.exclude(TalkYouTubeLink='').count()

	@property
	def url(self):
		return self.Name.replace(' ', '_')

	def __str__(self): return self.Name


globalCookie = None
globalCookieTime = datetime.now()


def getTicketsNumber():
	global globalCookie, globalCookieTime
	if globalCookie is None or (datetime.now() - globalCookieTime).total_seconds() > 3600:
		response = requests.post(
			url='https://payment.tuc.gr/admin.php',
			data={'username': 'TEDx2018', 'password': 'TED!@()2018', 'dologin': 'yes'}
		)
		globalCookie = response.cookies
		globalCookieTime = datetime.now()
	soup = BeautifulSoup(
		requests.get(
			url='https://payment.tuc.gr/admin.php?orderid=&txid=&datefrom=&dateto=&showfrom=1',
			cookies=globalCookie
		).text,
		"html.parser"
	)
	return soup.find_all('tr', {'class': 'captured'}).__len__()


class Ticket(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)
	Price = models.FloatField(default=0)
	Available = models.BooleanField(default=True)

	@property
	def isSoldOut(self): return False
		#  return getTicketsNumber() >= self.Event.TicketsNumber

	def __str__(self): return self.Name + ' - ' + self.Event.Name


class Position(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)

	def __str__(self): return self.Name + ' - ' + self.Event.Name


class TeamMember(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)
	Surname = models.CharField(max_length=100)
	Position = models.ForeignKey(Position, on_delete=models.SET_DEFAULT, default=1)
	email = models.CharField(max_length=100, blank=True)
	Telephone = models.IntegerField(null=True, blank=True)
	University = models.CharField(max_length=100, blank=True)
	School = models.CharField(max_length=100, blank=True)
	EducationalLevel = models.CharField(max_length=100, blank=True)
	ProfileImage = models.ImageField(default='TEDx2018/Shared/XWhite.svg', blank=True, upload_to='TEDx2018/TeamMemberProfilePictures/')
	ProfileImage2 = models.ImageField(blank=True, upload_to='TEDx2018/TeamMemberProfilePictures/')
	Bio = models.TextField(blank=True)
	Facebook = models.CharField(max_length=100, blank=True)
	GitHub = models.CharField(max_length=100, blank=True)
	GooglePlus = models.CharField(max_length=100, blank=True)
	Instagram = models.CharField(max_length=100, blank=True)
	LinkedIn = models.CharField(max_length=100, blank=True)
	Pinterest = models.CharField(max_length=100, blank=True)
	Reddit = models.CharField(max_length=100, blank=True)
	Twitter = models.CharField(max_length=100, blank=True)
	YouTube = models.CharField(max_length=100, blank=True)
	InternetLink = models.CharField(max_length=100, blank=True)

	@property
	def FullName(self): return self.Name + ' ' + self.Surname

	@property
	def HasLinks(self):
		return bool(self.Facebook) | bool(self.GitHub) | bool(self.GooglePlus) | bool(self.Instagram) | bool(self.LinkedIn) | bool(self.Pinterest) | bool(self.Twitter) | bool(self.YouTube) | bool(self.InternetLink)

	@property
	def url(self):
		return self.Name + '_' + self.Surname

	def __str__(self): return self.FullName


class Team(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)
	Photo = models.ImageField(default='TEDx2018/Shared/XBlackBig.svg', blank=True, upload_to='TEDx2018/TeamPhotos/')
	PhotoDescription = models.CharField(blank=True, max_length=100)

	def __str__(self): return self.Name + ' - ' + self.Event.Name


class TeamMemberAssignment(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	TeamMember = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
	Team = models.ForeignKey(Team, on_delete=models.CASCADE, default=1)

	def __str__(self): return str(self.TeamMember) + ' - ' + str(self.Team) + ' - ' + self.Event.Name


class Session(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)
	Time = models.TimeField(default="00:00")

	def __str__(self): return self.Name + ' - ' + self.Event.Name


class Speaker(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)
	Surname = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	Telephone = models.IntegerField(blank=True, null=True)
	ProfileImage = models.ImageField(default='TEDx2018/Shared/XWhite.svg', blank=True, upload_to='TEDx2018/SpeakerProfilePictures/')
	Title = models.CharField(max_length=100, blank=True)
	Bio = models.TextField(blank=True)
	AnnouncementDateTime = models.DateTimeField(default=None, blank=True, null=True)
	Session = models.ForeignKey(Session, default=1, null=True, on_delete=models.SET_NULL)
	TalkTime = models.TimeField(default=None, blank=True, null=True)
	HasSpoken = models.BooleanField(default=False, blank=True)
	Presentation = models.FileField(blank=True, upload_to='TEDx2018/SpeakerPresentations/')
	PresentationReleaseDateTime = models.DateTimeField(default=None, blank=True, null=True)
	PresentationRelease = models.BooleanField(default=False)
	Facebook = models.CharField(max_length=100, blank=True)
	GitHub = models.CharField(max_length=100, blank=True)
	GooglePlus = models.CharField(max_length=100, blank=True)
	Instagram = models.CharField(max_length=100, blank=True)
	LinkedIn = models.CharField(max_length=100, blank=True)
	Pinterest = models.CharField(max_length=100, blank=True)
	Reddit = models.CharField(max_length=100, blank=True)
	Twitter = models.CharField(max_length=100, blank=True)
	YouTube = models.CharField(max_length=100, blank=True)
	InternetLink = models.CharField(max_length=100, blank=True)
	TalkTitle = models.CharField(max_length=100, blank=True)
	TalkSummary = models.TextField(blank=True)
	TalkYouTubeLink = models.CharField(max_length=100, blank=True)

	@property
	def FullName(self): return self.Name + ' ' + self.Surname

	@property
	def Announced(self):
		return True if self.AnnouncementDateTime is None else self.AnnouncementDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple()

	@property
	def HasLinks(self):
		return bool(self.Presentation) | bool(self.Facebook) | bool(self.GitHub) | bool(self.GooglePlus) | bool(self.Instagram) | bool(self.LinkedIn) | bool(self.Pinterest) | bool(self.Twitter) | bool(self.YouTube) | bool(self.InternetLink)

	@property
	def url(self):
		return self.Name + '_' + self.Surname

	def __str__(self): return self.FullName + ' - ' + self.Event.Name


class Workshop(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	# Name = models.CharField(max_length=100)
	# Surname = models.CharField(max_length=100, blank=True)
	# email = models.CharField(max_length=100, blank=True)
	# Telephone = models.IntegerField(blank=True, null=True)
	ProfileImage = models.ImageField(default='TEDx2018/Shared/XWhite.svg', blank=True, upload_to='TEDx2018/SpeakerProfilePictures/')
	Title = models.CharField(max_length=100, blank=True)
	Description = models.TextField(blank=True)
	AnnouncementDateTime = models.DateTimeField(default=None, blank=True, null=True)
	Session = models.ForeignKey(Session, default=1, null=True, on_delete=models.SET_NULL)
	TalkTime = models.TimeField(default=None, blank=True, null=True)
	isMain = models.BooleanField(default=True, blank=True)
	HasSpoken = models.BooleanField(default=False, blank=True)
	Facebook = models.CharField(max_length=100, blank=True)
	GitHub = models.CharField(max_length=100, blank=True)
	GooglePlus = models.CharField(max_length=100, blank=True)
	Instagram = models.CharField(max_length=100, blank=True)
	LinkedIn = models.CharField(max_length=100, blank=True)
	Pinterest = models.CharField(max_length=100, blank=True)
	Reddit = models.CharField(max_length=100, blank=True)
	Twitter = models.CharField(max_length=100, blank=True)
	YouTube = models.CharField(max_length=100, blank=True)
	InternetLink = models.CharField(max_length=100, blank=True)

	# TalkTitle = models.CharField(max_length=100, blank=True)
	# TalkSummary = models.TextField(blank=True)
	# TalkYouTubeLink = models.CharField(max_length=100, blank=True)

	# @property
	# def FullName(self): return self.Name + ' ' + self.Surname

	@property
	def Announced(self):
		return True if self.AnnouncementDateTime is None else self.AnnouncementDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple()

	@property
	def HasLinks(self):
		return bool(self.Facebook) | bool(self.GitHub) | bool(self.GooglePlus) | bool(self.Instagram) | bool(self.LinkedIn) | bool(self.Pinterest) | bool(self.Twitter) | bool(self.YouTube) | bool(self.InternetLink)

	# @property
	# def url(self):
	# 	return self.Name + '_' + self.Surname

	def __str__(self): return self.Title + ' - ' + self.Event.Name


class PartnerLevel(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)
	Level = models.IntegerField(default=1, blank=True)

	def __str__(self): return self.Name + ' - ' + self.Event.Name


class Partner(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	CompanyName = models.CharField(max_length=100)
	PartnerLevel = models.ForeignKey(PartnerLevel, on_delete=models.CASCADE, default=1)
	Name = models.CharField(max_length=100, blank=True)
	Surname = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	Telephone = models.IntegerField(blank=True, null=True)
	Logo = models.ImageField(default='TEDx2018/Shared/XWhite.svg', blank=True, upload_to='TEDx2018/SponsorLogos/')
	AnnouncementDateTime = models.DateTimeField(default=None, blank=True, null=True)
	InternetLink = models.CharField(max_length=100, blank=True)

	@property
	def Announced(self):
		return True if self.AnnouncementDateTime is None else self.AnnouncementDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple()

	@property
	def HasLinks(self):
		return self.InternetLink

	def __str__(self): return self.CompanyName + ' - ' + self.Event.Name


class AboutUsCarouselPhoto(models.Model):
	Event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)
	Photo = models.ImageField(default='TEDx2018/Shared/XBlackBig.svg', blank=True, upload_to='TEDx2018/AboutUsCarouselPhotos/')
	Description = models.CharField(max_length=100, blank=True)

	def __str__(self): return self.Photo.name + ' - ' + self.Event.Name + ' - ' + self.Description
