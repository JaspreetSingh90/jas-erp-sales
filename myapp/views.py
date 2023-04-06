from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Customer, Order
from django.forms.models import model_to_dict
from myapp.forms import customer_form

def home(request):
    return render(request, "home.html")

def Customers(request, *args, **kwargs):
    customers = Customer.objects.values()
    return JsonResponse({'customers': list(customers)})

def customer_id(request, id):
    customer = Customer.objects.get(id = id)
    print(customer)
    return JsonResponse(model_to_dict(customer))


def add_customer(request):
    print(request.method)
    context = {}
    form = customer_form(request.POST or None)
    context['form'] = form
    if request.method == "POST":
        Customer.objects.create(name=request.POST.get('name'),email=request.POST.get('email'),phone=request.POST.get('phone'),address = request.POST.get('address'))
    
    return render(request, "customer.html", context)


def add_order(request):
    print(request.method)
    context = {}
    form = customer_form(request.POST or None)
    context['form'] = form
    if request.method == "POST":
        Order.objects.create(customer=request.POST.get('customer'),items=request.POST.get('items'),totalamount=request.POST.get('totalamount'),orderdate = request.POST.get('orderdate'))
        pass
    
    return render(request, "orders.html", context)


def order_id(request, id):
    order = Order.objects.get(id = id)
    print(order)
    return JsonResponse(model_to_dict(order))


def all_orders(request, *args, **kwargs):
    customers = Order.objects.values()
    return JsonResponse({'orders': list(customers)})