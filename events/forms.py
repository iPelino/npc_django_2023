from django import forms

from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "category",
            "start_date",
            "end_date",
            "venue",
            "is_fee"
        ]