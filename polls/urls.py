from django.urls import path

from . import views

urlpatterns = [
    ## one form create route
    path("", views.Index, name="Index"),
    path("one/", views.OptionOne, name="one"),
    path("two/", views.OptionTwo, name="two"),
    path("one/<int:question_id>/", views.questions, name="questions"),
    #path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
