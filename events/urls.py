from django.urls import path

from events import views

urlpatterns = [
    path('', views.events, name='events'),
    path('<str:name>', views.event_detail, name='event_detail') # 127.0.0.1:8000/events/PyCon
]