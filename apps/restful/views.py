from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User


def index(request):
    return render(request,"restful/index.html", {"dank": User.objects.all()})

def new(request):
    return render(request,"restful/new.html")

def edit(request,id):
    return render(request,"restful/edit.html", {"dank": User.objects.get(id=id)})

def show(request,id):
    return render(request,"restful/users.html", {"dank": User.objects.get(id=id)})

def create(request):
    if request.method == "POST":
        heyerrors = User.objects.dank_validator(request.POST)
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        if len(heyerrors):
            for key, value in heyerrors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/users/new')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            User.objects.create(first_name=first_name, last_name=last_name, email=email) 
            messages.success(request, "User Successfuly Created")
            id = str(User.objects.last().id)
            return redirect('/users/show/'+id)
    return redirect("/users")

def delete(request,id):
    b = User.objects.get(id=id)
    b.delete()
    return redirect("/users")

def update(request,id):
    if request.method == "POST":
        heyerrors = User.objects.dank_validator(request.POST)
        if len(heyerrors):
            for key, value in heyerrors.items():
                messages.error(request, value)
            return redirect('/users/edit/'+id)
        else:
            user = User.objects.get(id = id)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            messages.success(request, "User successfully updated")
            return redirect('/users')
    
    return redirect("/users")

