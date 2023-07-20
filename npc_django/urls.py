from django.contrib import admin
from django.urls import path, include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('events/', include('events.urls')),

]
