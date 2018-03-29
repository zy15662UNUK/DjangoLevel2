from django.shortcuts import render
from django.http import HttpResponse #import HttpResponse object

# Create your views here.

def index(request):
    # an view, each view must return in HttpResponse object
    return HttpResponse("<em>My second app</em>")

def help(request):
    my_dic = {"insert_me": "HELP PAGE"}
    return render(request,"AppTwo\index.html",context=my_dic)
