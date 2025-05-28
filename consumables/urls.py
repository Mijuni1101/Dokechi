from django.urls import path
from . import views

urlpatterns = [
    path("calendar/", views.calendar_view, name="calendar_view"),
    path("api/events/", views.calendar_events, name="calendar_events"),
]