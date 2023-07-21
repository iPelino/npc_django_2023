from django.shortcuts import render

from events.forms import EventForm
from events.models import Event


def events(request):
    # events =  ['PyCon', 'DjangoCon', 'PyData', 'EuroPython', 'SciPy']
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, pk):
    # events = ['PyCon', 'DjangoCon', 'PyData', 'EuroPython', 'SciPy']
    # lowered_events = [event.lower() for event in events]
    try:
        event = Event.objects.get(id=pk)  # select * from events_event where id = 1
        return render(request, 'events/event_details.html', {'event': event})
    except Event.DoesNotExist:
        return render(request, '404.html')





def add_event(request):
    form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})