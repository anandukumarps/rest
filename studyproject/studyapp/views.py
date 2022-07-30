from django.http import HttpResponse
from django.shortcuts import render
from .models import food

# Create your views here.
def test(request):
    obj = food.objects.all()
    return render(request,'index.html',{'item':obj})

