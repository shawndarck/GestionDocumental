from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'usuarios/login.html')


# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Hi {username}, Tu cuenta ha sido creada con exito!')
#             return redirect('home')
#     else:
#         form = UserRegisterForm()

#     return render(request, 'usuarios/register.html', {'form': form})


@login_required()
def sidebar(request):
    return render(request, 'usuarios/sidebar.html')
