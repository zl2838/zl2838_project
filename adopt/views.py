
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Pet

def all_pets(request):
    pets=Pet.objects.all()
    context ={
            'pets':pets,
            }
    return render(request,'adopt/all.html',context)

def pet_details(request,pet_id):
    pet=Pet.objects.get(id=pet_id)
    return HttpResponse(pet.name)


