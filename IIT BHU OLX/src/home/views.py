from django.shortcuts import render
from django.http import HttpResponseRedirect
from product.models import Product , Category
from home.forms import newad
# Create your views here.

def home(request):

    all_category = Category.objects.all()
    products = Product.objects.all()

    template = 'home.html'
    context = { 'all_category' : all_category , 'products' : products}

    return render(request , template , context)

def postad(request):
    # return render(request,'Product/postad.html',context={})
    if request.method=="POST":
        form=newad(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,'postad.html',{'form':newad})
    else:
        form_class=newad
        return render(request,'postad.html',{'form':form_class})
