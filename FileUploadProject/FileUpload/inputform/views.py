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
    # A HTTP POST?
    if request.method == 'POST':
        form = UserNameForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            return index(request)

            # Now call the index() view.
            # The user will be shown the homepage.
        else:
            return form.errors
    else:
        form = UserNameForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('inputform/add_username.html', {'form': form}, context)
	