from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import ListView, DeleteView, DetailView
from .models import *
from . forms import *

# Create your views here.

def base(request):
    return render(request,'app/base.html')

def detail(request):
    return render(request, 'app/detail.html')


def home(request):
    vehicles = Vehicle.objects.all() 
    return render(request, 'app/home.html',{'vehicles': vehicles})

def brand(request):

    brands = Brand.objects.all()
    
    return render(request, 'app/brands.html', {'brands':brands})

class VehicleListView(ListView):
    model = Vehicle
    form_class = VehicleListForm
    template_name = 'app/vehicle_list.html'
    context_object_name = 'vehicles'

def create_vehicle(request):
    if request.method == "POST":
        form = CreateVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Created')
            return redirect('vehicle list')           
    else:
        form = CreateVehicleForm()

    return render(request, 'app/create_vehicle.html', {'form':form})

def update_vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == "POST":
        form = CreateVehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, f'Updated')
            return redirect('vehicle list')
    else:
        form = CreateVehicleForm(instance=vehicle)
        
    return render(request, 'app/update_vehicle.html', {'form':form, 'vehicle':vehicle})

def delete_vehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    vehicle.delete()
    return redirect('vehicle list')
    

class DeleteVehicleView(DeleteView):
    model = Vehicle
    template_name = 'app/delete_vehicle.html'
    context_object_name = 'vehicle'
    success_url = reverse_lazy('vehicle list')

class VehicleView(DetailView):
    model = Vehicle
    template_name = 'app/detail.html'
    context_object_name = 'vehicle'
    success_url = reverse_lazy('vehicle list')  
