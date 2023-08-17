from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('username')
            Password = form.cleaned_data.get('password')
            user = authenticate(username=Username, password=Password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).image.url
                except:
                    avatar = '/static/img/avatar/user_default.png'
                finally:
                    request.session['avatar'] = avatar
                return render(request, "home.html", {"mensaje": f"Bienvenido {Username}"})
            else:
                return render(request, "users/login.html", {"form":form, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "users/login.html", {"form":form, "mensaje": "Datos Inválidos"})
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form":form})  


def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html", {"mensaje":"Usuario Creado"})        
    else:
        form = UserCreateForm()
    return render(request, "users/user_create.html", {"form": form})   

@login_required
def user_update(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.user = form.cleaned_data.get('username')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return render(request, "home.html", {'mensaje': f"Usuario {user.username} Actualizado"})
        else:
            return render(request, "users/user_update.html", {'form': form})
    else:
        form = UserUpdateForm(instance=user)
    return render(request, "users/user_update.html", {'form': form, 'user':user.username})


@login_required
def user_avatar(request):
    if request.method == "POST":
        form = UserAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            users = User.objects.get(username=request.user)
            avatar_old = Avatar.objects.filter(user=users)
            if len(avatar_old) > 0:
                avatar_old[0].delete()
            avatar = Avatar(user=users, image=form.cleaned_data['image'])
            avatar.save()
            image = Avatar.objects.get(user=request.user.id).image.url
            request.session['avatar'] = image
            return render(request, "base.html")
    else:
        form = UserAvatarForm()
    return render(request, "users/user_avatar.html", {'form': form})

# listamos todos las categorias
@login_required
def user_list (request):
    users = User.objects.order_by('first_name')
    context = {
        'users': users,
    }
    return render(request, 'users/user_list.html', context)

# Eliminamos una categoria con el id seleccionado
@login_required
def user_delete(request, id):
    users = User.objects.get(pk = id)
    if request.method == 'POST':
        users.delete()
        return redirect('user_list')
    context = {'users': users}
    return render(request, 'users/user_delete.html', context)

