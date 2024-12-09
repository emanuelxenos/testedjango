from django.shortcuts import render, redirect
from .models import People

# Create your views here.
def home(request):
    people = People.objects.all()
    return render(request,'index.html',{'peoples':people})

def init(request):
    return render(request,'home.html')

def salvar(request):
    fullname = request.POST.get('fullname')
    years = request.POST.get('years')
    email = request.POST.get('email')
    if not request.POST.get('id'):
        print('Não tem id então posso salvar')
        People.objects.create(fullname = fullname, years = years, email = email)
    else:
        fullname = request.POST.get('fullname')
        years = request.POST.get('years')
        email = request.POST.get('email')
        people = People.objects.get(id=request.POST.get('id'))
        people.fullname = fullname
        people.years = years
        people.email = email
        people.save()
    return redirect(home)    
    # peoples = People.objects.all()
    # return render(request,"index.html",{"peoples":peoples})

def editar(request,id):
    people = People.objects.get(id=id)
    return render(request,'update.html',{"people":people})

def register(request):
    return render(request,'register.html')

def update(request,id):
     return redirect(home)

def apagar(resquest, id):
    people = People.objects.get(id=id)
    people.delete()
    return redirect(home)