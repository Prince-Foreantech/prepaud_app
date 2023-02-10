from django.shortcuts import render
from .models import subcategory,category,audiofile
# Create your views here.
from django.http import HttpResponse
import json

def get_subcategory(request):

    data = audiofile.objects.all()
    return render(request,"change_form.html",{'data':data})
