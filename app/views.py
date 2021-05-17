from app.models import Veiculo
from django.shortcuts import render, redirect
from app.forms import VeiculoForm



def home(request):
    return render(request, 'home.html')

def veiculos(request):
    data = {}
    data['db'] = Veiculo.objects.all()
    return render(request, 'veiculos.html', data)

def clientes(request):
    return render(request, 'clientes.html')

def vendas(request):
    return render(request, 'vendas.html')

def form(request):
    data = {}
    data['form'] = VeiculoForm()
    return render(request, 'form.html', data)

def create(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('veiculos')

def view(request, pk):
    data = {}
    data['db'] = Veiculo.objects.get(pk=pk)
    return render(request, 'view.html', data )

def edit(request, pk):
    data = {}
    data['db'] = Veiculo.objects.get(pk=pk)
    data['form'] = VeiculoForm(instance=data['db'])
    return render(request, 'form.html', data )

def update(request, pk):
    data = {}
    data['db'] = Veiculo.objects.get(pk=pk)
    form = VeiculoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('veiculos')

def delete(request, pk):
    db = Veiculo.objects.get(pk=pk)
    db.delete()
    return redirect('veiculos')
