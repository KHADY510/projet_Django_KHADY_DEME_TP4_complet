from django.shortcuts import render


def accueil(request):
    return render(request, "pages/accueil.html")


def home(request):
    return render(request, "pages/home.html")


def course_list(request):
    return render(request, "pages/courses.html")


def about(request):
    return render(request, "pages/about.html")
