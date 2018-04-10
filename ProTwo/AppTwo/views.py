from django.shortcuts import render
from django.http import HttpResponse #import HttpResponse object
from AppTwo.models import User
# Create your views here.

def index(request):
    # an view, each view must return in HttpResponse object
    return HttpResponse("<em>My second app</em>")

def user(request):
    user_list = User.objects.order_by('last_name')
    my_dic = {"user": user_list}
    return render(request,"AppTwo\index.html",context=my_dic)
