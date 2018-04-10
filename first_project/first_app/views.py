from django.shortcuts import render
from django.http import HttpResponse #import HttpResponse object
from first_app.models import Topic,Webpage,AccessRecord#import models
# Create your views here.

def index(request):
    # an view, each view must return in HttpResponse object
    webpages_list = AccessRecord.objects.order_by('date')# order the AccessRecord by 'data' column
    date_dict = {'accss_records':webpages_list}# content to be inserted into template
    # {"insertNameSameAsIndexHTML":"InsertContent"}
    return render(request,"first_app/index.html",context=date_dict)# render(request,templateDir,context)
    # return HttpResponse("hello world")
