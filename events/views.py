from django.shortcuts import render_to_response, get_object_or_404, redirect
from events.models import Events
from django.template import RequestContext
# Create your views here.
def index(request):
    return redirect('event')


def event(request):
    events = Events.objects.order_by('id')
    return render_to_response(
        'events/events.html',
        {'events': events},
		context_instance=RequestContext(request)
    )
def event_detail(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render_to_response(
        'events/events_detail.html',
        {'event': event},
        context_instance=RequestContext(request)
    )