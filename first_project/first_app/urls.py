from django.conf.urls import url
from first_app import views
# urls.py file set up for the individual app
urlpatterns = [
    url(r'^$',views.index,name="index"),# generic regular expression
]
