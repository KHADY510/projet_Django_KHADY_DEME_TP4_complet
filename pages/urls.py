from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("home/", views.home, name="home"),
    path("courses/", views.course_list, name="courses"),
    path("about/", views.about, name="about"),
]
