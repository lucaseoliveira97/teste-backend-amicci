from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoriesListView.as_view(), name="categories-view"),
    path("category/", views.CategoryCreateView.as_view(), name="category-create"),
    path("category/<int:pk>", views.CategoryRetrieveUpdateView.as_view(), name="category-retrieve-update")
]

