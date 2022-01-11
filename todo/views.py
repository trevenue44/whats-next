from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "todo/home.html", context=context)
