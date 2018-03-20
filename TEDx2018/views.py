from django.shortcuts import render

from TEDx2018.models import Event


def home(request):
	# events = Event.objects.filter(StartDateTime__lte=datetime.now()).order_by('-StartDateTime')
	events = Event.objects.order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/home.html', context={'events': events})


def currentEvent(request):
	return render(request=request, template_name='TEDx2018/404.html')


def upcomingEvents(request):
	return render(request=request, template_name='TEDx2018/404.html')


def previousEvents(request):
	return render(request=request, template_name='TEDx2018/404.html')


def talks(request):
	return render(request=request, template_name='TEDx2018/talks.html')


def speakers(request):
	return render(request=request, template_name='TEDx2018/speakers.html')


def partners(request):
	return render(request=request, template_name='TEDx2018/partners.html')


def becomeAPartner(request):
	return render(request=request, template_name='TEDx2018/becomeAPartner.html')


def community(request):
	return render(request=request, template_name='TEDx2018/community.html')


def joinAsAMember(request):
	return render(request=request, template_name='TEDx2018/joinAsAMember.html')


def donors(request):
	return render(request=request, template_name='TEDx2018/donors.html')


def becomeADonor(request):
	return render(request=request, template_name='TEDx2018/becomeADonor.html')


def about(request):
	return render(request=request, template_name='TEDx2018/about.html')


def ourTeam(request):
	return render(request=request, template_name='TEDx2018/ourTeam.html')


def contactUs(request):
	return render(request=request, template_name='TEDx2018/contactUs.html')


def becomeAVolunteer(request):
	return render(request=request, template_name='TEDx2018/becomeAVolunteer.html')


def faq(request):
	return render(request=request, template_name='TEDx2018/faq.html')


def custom_404(request):
	return render(request=request, template_name='TEDx2018/404.html')


def custom_500(request):
	return render(request=request, template_name='TEDx2018/500.html')
