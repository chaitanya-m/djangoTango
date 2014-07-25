from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from inputform.forms import UserNameForm

def index(request):
    return HttpResponse("Hello World!")

def add_username(request):
    # Get the context from the request.
    context = RequestContext(request)

    form = UserNameForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('inputform/add_username.html', {'form': form}, context)
	