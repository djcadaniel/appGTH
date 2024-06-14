from django.shortcuts import render, redirect
from .models import Contratos
from .forms import ContratosForm
from django.contrib import messages
# Create your views here.
def index(request):
  contratos = Contratos.objects.filter(name__contains=request.GET.get('search', ''))
  context = {
    'contratos': contratos
  }
  return render(request, 'contratos/index.html', context)

def view(request, id):
  contratos = Contratos.objects.get(id=id)
  context = {
    'contratos': contratos
  }
  return render(request, 'contratos/detail.html', context)

def edit(request, id):
  contratos = Contratos.objects.get(id=id)

  if(request.method == 'GET'):
    form = ContratosForm(instance = contratos)
    context = {
      'form': form,
      'id':id
    }
    return render(request, 'contratos/edit.html', context)
  
  if request.method == 'POST':
    form = ContratosForm(request.POST, instance= contratos)
    if form.is_valid():
      form.save()
    context ={
      'form': form,
      'id': id
    }
    messages.success(request, 'Mensaje actualizado')
    return render(request, 'contratos/edit.html', context)
  
def create(request):
  if request.method == 'GET':
    form = ContratosForm()
    context = {
      'form': form
    }
    return render(request, 'contratos/create.html', context)
  
  if request.method == 'POST':
    form = ContratosForm(request.POST)
    if form.is_valid:
      form.save()
    return redirect('contratos')

def delete(request, id):
  contratos = Contratos.objects.get(id=id)
  contratos.delete()
  return redirect('contratos')