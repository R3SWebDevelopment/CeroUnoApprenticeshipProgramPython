from django.shortcuts import render
from django.contrib.auth.decorators import login_required
"""@login_required 
def my_view(request):
    ..."""

def index(request):
    return render(request, "personas/index.html")

def pag1(request):
    return render(request, "personas/pag1.html")

def pag2(request):
    return render(request, "personas/pag2.html")

def pag3(request):
    return render(request, "personas/pag3.html")

def pag4(request):
    return render(request, "personas/pag4.html")
def pag5(request):
    return render(request, "personas/pag5.html")    

def pag6(request):
    return render(request, "personas/pag6.html") 
def pag7(request):
    return render(request, "personas/pag7.html") 
def pag8(request):
    return render(request, "personas/pag8.html") 
def pag9(request):
    return render(request, "personas/pag9.html")
def pag10(request):
    return render(request, "personas/pag10.html")  
def pag11(request):
    return render(request, "personas/pag11.html")
def pag12(request):
    return render(request, "personas/pag12.html")
def pag13(request):
    return render(request, "personas/pag13.html")
def pag14(request):
    return render(request, "personas/pag14.html")
def pag15(request):
    return render(request, "personas/pag15.html")
def pag16(request):
    return render(request, "personas/pag16.html")
def pag17(request):
    return render(request, "personas/pag17.html")
def pag18(request):
    return render(request, "personas/pag18.html")
def pag19(request):
    return render(request, "personas/pag19.html")
def pag20(request):
    return render(request, "personas/pag20.html")
def pag21(request):
    return render(request, "personas/pag21.html")
def pag22(request):
    return render(request, "personas/pag22.html")                 
def UNIDAD1(request):
    return render(request, "personas/UNIDAD1.html")
def UNIDAD2(request):
    return render(request, "personas/UNIDAD2.html")
def UNIDAD3(request):
    return render(request, "personas/UNIDAD3.html")
def UNIDAD4(request):
    return render(request, "personas/UNIDAD4.html")
def UNIDAD5(request):
    return render(request, "personas/UNIDAD5.html")          
def UNIDAD6(request):
    return render(request, "personas/UNIDAD6.html")
def UNIDAD7(request):
    return render(request, "personas/UNIDAD7.html") 