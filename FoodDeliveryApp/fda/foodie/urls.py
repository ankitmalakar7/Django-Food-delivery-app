from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("search/", views.search, name="search"),
    path("view/<int:food_id>", views.view, name="view"),
    path("checkout/", views.checkout, name="checkout"),
]
