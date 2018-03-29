from django.shortcuts import render
from django.http import HttpResponse #import HttpResponse object

# Create your views here.

def index(request):
    # an view, each view must return in HttpResponse object
    my_dict = {"insert_me": "Hello I am James"} # content to be inserted into template
    # {"insertNameSameAsIndexHTML":"InsertContent"}
    return render(request,"first_app/index.html",context=my_dict)# render(request,templateDir,context)
    # return HttpResponse("hello world")
