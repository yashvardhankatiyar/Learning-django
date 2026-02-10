from django.shortcuts import render, redirect
from .models import Note


def noteAppHome(request):
    notes = Note.objects.all().order_by("-created_by")
    return render(request, "index.html", {"notes": notes})


def add_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Note.objects.create(title=title)
    return redirect("home")


def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return redirect("home")


def edit_note(request, id):
    if request.method == "POST":
        note = Note.objects.get(id=id)
        note.title = request.POST.get("title")
        note.save()
    return redirect("home")
