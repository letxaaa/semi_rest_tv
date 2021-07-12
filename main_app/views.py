from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect("/shows/new")

def validate(request):
    print(request.POST)
    return JsonResponse({"res":"hello!!"})

def dash(request):
    context = {
        'all_shows':Show.objects.all()
    }
    return render(request, "dashboard.html", context)
def new(request):
    if request.method == "GET":
        return render(request, "index.html")
    if request.method == "POST":
        errors = Show.objects.validate_show(request.POST)

        if len(errors):
            for key, val in errors.items():
                messages.error(request, val)
            return redirect("/shows/new")
        
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']

        new_show = Show.objects.create(title = title, network = network, release_date = release_date, description = description)
        print(new_show)
        return redirect("/shows/"+str(new_show.id))
    
def show(request, show_id):
    context = {
        "show" : Show.objects.get(id = show_id)
    }
    return render(request, "show.html", context)

def edit(request, show_id):
    context = {
        "show" : Show.objects.get(id = show_id)
    }
    return render(request, "edit.html", context)

def delete(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect("/shows")