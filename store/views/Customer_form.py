from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.Customer_form import Contact1
from django.views import  View
from store.models.customer import Customer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def contact1(request):
    if request.method=="POST":
        Relation = request.POST.get('Relation', '')
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        category = request.POST.get('category', '')
        customer1 = Customer.objects.filter(id=request.session.get('customer'))[0]
        contact1 = Contact1(Relation=Relation, name=name, dob=dob, category=category,customer=customer1)
        contact1.save()
        print(customer1)
    return render(request, 'Customer_form.html')