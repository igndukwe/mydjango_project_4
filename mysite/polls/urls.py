from django.urls import path

from . import views

# @Anyi this is good for saparating concerns
# e.g. polls has name="detail" and another
# app sales might also have name="detail"
app_name = "polls"
urlpatterns = [
    # @Anyi: Home page should take you to this place e.g. anyioneta.com
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# app_name = 'another_app'
# urlpatterns = [ ]

