from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    # path("about/", views.index, name="about"),
    # path("contact/", views.contact, name="contact"),
    # path("search/", views.search, name="search"),
    # path("tracker/", views.tracker, name="tracker"),
    # path("view/", views.view, name="view"),
    # path("checkout/", views.checkout, name="checkout"),
]
