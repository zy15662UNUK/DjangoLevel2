from django.contrib import admin
from first_app.models import AccessRecord,Topic,Webpage
# import all the classes from the model
# Register your models here.
# tell the app the models exist
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
# Then need to create a superuser, with username, email and password
# access admin by "http://127.0.0.1:8000/admin/"
# Then we could see the models we just created
