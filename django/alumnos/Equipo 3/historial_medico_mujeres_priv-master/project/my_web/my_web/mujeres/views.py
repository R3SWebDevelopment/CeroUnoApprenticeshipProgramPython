from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .forms import MujerForm


from .models import Mujer

from .forms import MujerForm

def print_mujeres(request):
    if request.method == "POST":
        form = MujerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/mujeres/")
    else:
        form = MujerForm()

    mujeres = Mujer.objects.all()
    context = {
        'lista_mujeres': mujeres,
        'form': form
    }
    return render(request, 'mujeres/listar_mujeres.html', context)

def print_ruben_test(request):

    if request.method == "POST":
        form = MujerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/mujeres/")
    else:
        form = MujerForm()

    mujeres = Mujer.objects.all()
    context = {
        'lista_mujeres' : mujeres,
        'form': form
    }
    return render(request, 'mujeres/tst_ruben.html', context)