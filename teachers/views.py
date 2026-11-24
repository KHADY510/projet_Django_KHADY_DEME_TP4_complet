from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TeacherForm
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teacher_list.html", {"teachers": teachers})


def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            messages.success(request, f"{teacher} a été ajouté(e).")
            return redirect("teachers:list")
    else:
        form = TeacherForm()
    context = {"form": form, "title": "Ajouter un enseignant"}
    return render(request, "teachers/teacher_form.html", context)


def teacher_update(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, f"La fiche de {teacher} a été mise à jour.")
            return redirect("teachers:list")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "teachers/teacher_form.html", {
        "form": form, "title": f"Modifier {teacher}", "teacher": teacher,
    })


def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        name = str(teacher)
        teacher.delete()
        messages.success(request, f"{name} a été supprimé(e).")
        return redirect("teachers:list")
    return render(request, "teachers/teacher_confirm_delete.html", {"teacher": teacher})
