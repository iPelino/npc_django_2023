from django.urls import path

from events import views

urlpatterns = [
    path('', views.events, name='events'),
    path('add', views.add_event, name='add_event'),  # 120.0.0.1:8000/events/add
    path('<str:name>', views.event_detail, name='event_detail'), # 127.0.0.1:8000/events/PyCon
]