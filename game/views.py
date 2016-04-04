from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm

def settings(request):

    return render(request, "settings.html", {})

def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/settings/')
    else:
        form = LoginForm()

    return render(request, "login.html", {'form':form})
