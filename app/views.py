from django.shortcuts import render
from app.models import *

# Create your views here.
def table(request):
    lo=Course.objects.all()
    d={'course':lo}
    return render(request,'table.html',context=d)
def display_student(request):
    xo=Student.objects.all()
    s={'student':xo}
    return render(request,'display_student.html',s)
