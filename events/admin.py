from django.contrib import admin
from events.models import Event, Category


class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "start_date", "end_date"]
    search_fields = ["start_date"]
    list_filter = ["category__name"]


admin.site.register(Event, EventAdmin)
admin.site.register(Category)
