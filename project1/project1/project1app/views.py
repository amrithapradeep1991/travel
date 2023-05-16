from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
#def demo(request):
#    return HttpResponse('hello world')
#def demo(request):
    #name="india"
   # return render(request,"home.html",{'obj':name})
#def about(request):
    #return render(request,"about.html")
#def contacts(request):
   # return HttpResponse('this is multiple views')
#def home(request):
  #  return render(request,"passingvalue.html")
#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
   # res=x+y
   # return render(request,"result.html",{'result':res})

# def home(request):
#     return render(request,"index.html")
#dynamic data passing
def home(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})
def team(request):
    them=Team.objects.all()
    return render(request,"index.html",{'members':them})