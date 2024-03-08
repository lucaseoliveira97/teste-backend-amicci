from django.urls import path
from . import views

urlpatterns = [
    path("vendors/", views.VendorsListView.as_view(), name="vendors-view"),
    path("vendor/", views.VendorCreateView.as_view(), name="vendor-create"),
    path("vendor/<int:pk>", views.VendorRetrieveUpdateView.as_view(), name="vendor-retrieve-update")
]

