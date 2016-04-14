from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Brand, ActiveSubstance, Classification, Medicine, ActiveSubstances
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

def game(request):
    test = ""
    for e in ActiveSubstance.objects.using('medicin').all():
        print(e.substance)
        test += e.substance + " "
    return render(request, "game.html", {'test' : test})
