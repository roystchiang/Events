from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from backend.forms import newEventForm
from events.models import Events

# Create your views here.
def user_login(request):
    context = RequestContext(request)
    # see the context of the request

    # If the request is a HTTP POST, we shall use the info.
    if request.method == 'POST':
        # Get the data you need
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to login
        user = authenticate(username=username, password=password)
        # If we have a user object, the details are correct
        if user:
            if user.is_active:
                # Check to see if the user is active
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # If not active, no login for you!
                return HttpResponse("Your account has been disabled.")
        else:
            # Bad login information was provided
            print "Invalid login info: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details provided.")
    else:
        # Not a HTTP POST request
        return render_to_response('backend/login.html', {}, context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def backend(request):
    context = RequestContext(request)
    if request.method == 'POST':
        # Attempt to grab information from the form
        newEvent_Form = newEventForm(request.POST, request.FILES)
        if newEvent_Form.is_valid():
            # If the form is correctly filled out
            event = Events(name = request.POST['name'], address = request.POST['address'], map_lon = request.POST['map_lon'], map_lat = request.POST['map_lat'],
                           start_date = request.POST['start_date'], description = request.POST['description'], end_date = request.POST['end_date'])
            if 'picture' in request.FILES:
                event.picture = request.FILES['picture']
            event.save()
        else:
            return HttpResponse(newEvent_Form)
    else:
        eventlist = Events.objects.order_by('id')
    return render_to_response("backend/backend.html", {}, context
    )
