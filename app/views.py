from django.shortcuts import render
from app.models import *

# Create your views here.
def table(request):
    lo=Course.objects.all()
    d={'course':lo}
    return render(request,'table.html',context=d)
