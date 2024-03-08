from django.urls import path
from . import views

urlpatterns = [
    path("briefings/", views.BriefingsListView.as_view(), name="briefing-view"),
    path("briefing/", views.BriefingCreateView.as_view(), name="briefing-create"),
    path("briefing/<int:pk>", views.BriefingRetrieveUpdateView.as_view(), name="briefing-retrieve-update")
]


