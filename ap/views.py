from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.

def Index(request):
    if 'each' in request.GET:
        each = request.GET['each']
        data = Data.objects.filter(last_name__icontains=each)
        all_data = Q(Q(first_name__icontains=each) | Q(last_name__icontains=each) | Q(age__icontains=each))
        data= Data.objects.filter(all_data)
    else:
        data = Data.objects.all()
    context = {
        'data': data
    }
    return render(request,'index.html',{"data":data})

def Nav(request):
    return render(request,'nav.html')