from django.shortcuts import render, redirect
from .tasks import test_task


def home(request):
    return render(request, "home.html")


def run_task(request):
    test_task.delay()
    return redirect("/")
