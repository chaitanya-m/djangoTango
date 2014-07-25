from django.shortcuts import render
from django.http import HttpResponse
from inputform.forms import UserNameForm

def index(request):
	return HttpResponse("Hello World!")
