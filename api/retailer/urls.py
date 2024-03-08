from django.urls import path
from . import views

urlpatterns = [
    path("retailers/", views.RetailersListView.as_view(), name="retailers-view"),
    path("retailer/", views.RetailerCreateView.as_view(), name="retailer-create"),
    path("retailer/<int:pk>", views.RetailerRetrieveUpdateView.as_view(), name="retailer-retrieve-update")
]

