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
    path('users/', include('django.contrib.auth.urls')), # new
    # multiple urls
    # users/logi
    # users/logout
    # users/password_change
    # users/password_change/done
    # users/password_reset
    # users/password_reset/done
    # users/reset/<uidb64>/<token>/

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
