from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect("login")
    return render(request, "../templates/register.html", {"UserCreationForm": form})