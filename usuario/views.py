from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import registroForm, loginForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login


# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Hola {username}! Como estas hoy?')
            return redirect("/tomaDatos/")
    else:
        form = registroForm()
    contexto = {
        "form":form
    }
    return render(request, "registro.html",contexto)

def login(request):
    # Creamos el formulario de autenticación vacío
    form = loginForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = loginForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                username = form.cleaned_data['username']
                messages.success(request, f'Hola {username}! Como estas hoy?')
                return redirect('/tomaDatos/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})