from django.conf.urls import url
from AppTwo import views
# urls.py file set up for the individual app
urlpatterns = [
    url(r'^$',views.user,name="user"),# generic regular expression
]
