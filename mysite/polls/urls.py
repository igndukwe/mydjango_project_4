from django.urls import path

from . import views

# @Anyi: Home page should take you to this place e.g. anyioneta.com
urlpatterns = [path("", views.index, name="index")]
