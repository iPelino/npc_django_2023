from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views
from npc_django import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('events/', include('events.urls')),

]+ static(settings.STATIC_URL)
