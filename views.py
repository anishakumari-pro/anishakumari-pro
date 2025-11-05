from django.shortcuts import render
from app.forms import *

# Create your views here
def insert_Student(request):
    ESTMFO=StudentModelForm()
    d={'ESTMFO':ESTMFO}

        

    return render (request,"insert_Student.html",d)

