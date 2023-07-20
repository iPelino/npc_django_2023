from django.shortcuts import render

from events.models import Event


def events(request):
    # events =  ['PyCon', 'DjangoCon', 'PyData', 'EuroPython', 'SciPy']
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, name):
    events = ['PyCon', 'DjangoCon', 'PyData', 'EuroPython', 'SciPy']
    # lowered_events = [event.lower() for event in events]
    if name in events:
        return render(request, 'events/event_details.html', {'name': name})
    else:
        return render(request, 'events/event_details.html', {'error': 'Event not found'})