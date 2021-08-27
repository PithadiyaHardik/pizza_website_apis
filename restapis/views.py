from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Pizzas
from rest_framework import generics
from .Serializers import PizzasSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json
# Create your views here.


# store the pizza
def store_pizza(request):
    if(request.method=='GET'):
        return render(request, 'store_pizza.html')
    if(request.method=='POST'):
        size=request.POST['size']
        topping=request.POST['topping']
        type1=request.POST['type']
        present=Pizzas.objects.filter(pizza_type=type1).filter(pizza_topping=topping).filter(pizza_size=size)
        if(present):
             return render(request, 'store_pizza.html',{'message':'Pizza already exist'})

        else:
            pizza=Pizzas(pizza_size=size,pizza_topping=topping,pizza_type=type1)

            pizza.save()

            return render(request, 'store_pizza.html',{'message':'Pizza added successfully'})


#API to list all the pizzas in the database

class show_all(generics.ListAPIView):
    queryset=Pizzas.objects.all()
    serializer_class=PizzasSerializer

#API to update the pizzas in the database

class update_pizza(generics.UpdateAPIView):
    lookup_field='id'
    queryset=Pizzas.objects.all()
    serializer_class=PizzasSerializer

#API to delete the pizza in the database

class delete_pizza(generics.DestroyAPIView):
    lookup_field='id'
    queryset=Pizzas.objects.all()
    serializer_class=PizzasSerializer


#APi to order the pizza

@api_view(['post'])
def add_order(request): 
    typ=request.data.get('pizza_type')
    size=request.data.get('pizza_size')
    topping=request.data.get('pizza_topping')
    if Pizzas.objects.filter(pizza_topping=topping).filter(pizza_type=typ).filter(pizza_size=size):
        return JsonResponse({"message":"Thank you"})
    else:
        return JsonResponse({"message":"Pizza not available"})


