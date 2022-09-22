from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.forms import inlineformset_factory
from . forms import OrderForm
from . filters import OrderFilter
# Create your views here.

def home(request):
    orders = order.objects.all()
    customers = Customer.objects.all()

    totalorders =orders.count()
    totalcustomers =customers.count()

    delivered = orders.filter(status="delivered").count()
    pending = orders.filter(status="Pending").count()

    context ={"orders":orders,"customers":customers,"totalorders":totalorders,
              "totalcustomers":totalcustomers,"delivered":delivered,"pending":pending}
    return render(request,"accounts/home.html",context)

def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders =customer.order_set.all()
    filter_order = OrderFilter(request.GET,queryset=orders)
    orders = filter_order.qs
    context ={"customer":customer,"orders":orders,"filter_order":filter_order}
    return render(request,"accounts/customers.html",context)

def products(request):
    products = Product.objects.all()
    context ={"products":products}
    return render(request,"accounts/products.html",context)

def addorder(request,pk):
    customer = Customer.objects.get(id=pk)
    OrderFormSet = inlineformset_factory(Customer,order,fields=('product','status'))
    formset = OrderFormSet(request.POST or None, queryset = order.objects.none() , instance=customer)
    #form = OrderForm(request.POST or None , initial={"customer":customer})
    if request.method == 'POST':
        formset = OrderForm(request.POST or None)
        if formset.is_valid():
            formset.save()
            return redirect("/")
    context ={"formset":formset}
    return render(request,"accounts/order_form.html",context)

def updateorder(request,pk):
    orders = order.objects.get(id=pk)
    form= OrderForm(request.POST or None,instance=orders)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")
    context ={"form":form}
    return render(request,"accounts/order_form.html",context)         

def deleteorder(request,pk):
    orders = order.objects.get(id=pk)
    if request.method == 'POST':
        orders.delete()
        return redirect("/")
    context ={"orders":orders}    
    return render(request,"accounts/delete.html",context)    