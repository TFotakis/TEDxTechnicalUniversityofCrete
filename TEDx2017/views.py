from django.shortcuts import render


def home(request):
	return render(request=request, template_name='TEDx2017/index.html')


def partners(request):
	return render(request=request, template_name='TEDx2017/partners.html')


def team(request):
	return render(request=request, template_name='TEDx2017/team.html')


def googleVerification(request):
	return render(request=request, template_name='TEDx2017/google19e14184e6149603.html')
