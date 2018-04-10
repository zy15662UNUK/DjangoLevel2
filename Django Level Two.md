https://docs.djangoproject.com/en/2.0/intro/tutorial02/
##### Creating models
1. Add classes in "\first_app\models.py":

```
from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)
    # Limit the input value length, unique=True make the Topic unique
    def __str__(self):
        return self.top_name
class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    # grab key from Topic
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

```
- The name of each Field instance (e.g. name or date) is the field’s name, in machine-friendly format. You’ll use this value in your Python code, and your database will use it as the column name.

2. In the cmd input:

  1. `python manage.py migrate`

  2. `python manage.py makemigrations first_app` first_app is the app name
    By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

  3. `python manage.py migrate`to create those model tables in your database
    The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

3. Register your models in "first_app\admin.py":

```
from django.contrib import admin
from first_app.models import AccessRecord,Topic,Webpage
# import all the classes from the model
# Register your models here.
# tell the app the models exist
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
```

4. Set up the superuser in cmd:

- Then need to create a superuser, with username, email and password
- `python manage.py createsuperuser`
- access admin by "http://127.0.0.1:8000/admin/"
- Then we could see the models we just created

##### Population scripts
- Once we’ve set up the models, it’s always good idea to populate them with sometest data
- We will use a library to help with this called Faker and create a script to do this.

1. First need to install Faker library by `pip install Faker` in cmd

2. Create "\populate_first_app.py"(same stage as manage.py)

```
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
# configuring the settings for the project

import django
django.setup()

## Fake POP script
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker
fakegeneration = Faker()
topics = ['search','social','marketplace','news','games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    # returns a tuple, Returns a tuple of (object, created),
    # where object is the retrieved or created object and created is a boolean specifying
    # whether a new object was created. only need the first item(object) is what we need
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegeneration.url()
        fake_date = fakegeneration.date()
        fake_name = fakegeneration.company()

        # create the new Webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create the fake access for the Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
        # topic=top, name=webpg attention! need to pass in the whole object, not just a str
if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")
```
- e.x. `Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]`
the parameter should be equal to the attrs of class webpage in models.py

3. Run the populate_first_app.py `python populate_first_app.py`

4. `python manage.py runserver` to check

##### Models-Templates-Views Paradigm
- There are a few basics steps to achieving the goal of serving dynamic content to a user based off the connection of the models, views , and templates.

1. In the views.py file import any models taht we will need to use

`from first_app.models import Topic,Webpage,AccessRecord`

2. use the view to query the model for data we will need

```
def index(request):
    # an view, each view must return in HttpResponse object
    webpages_list = AccessRecord.objects.order_by('date')# order the AccessRecord by 'data' column
    date_dict = {'accss_records':webpages_list}# content to be inserted into template
    # {"insertNameSameAsIndexHTML":"InsertContent"}
    return render(request,"first_app/index.html",context=date_dict)# render(request,templateDir,context)
    # return HttpResponse("hello world")

```

3. pass results from the model to the template
- in index.html:

```
{% if accss_records %}
  <table>
    <thead>
      <th>Site name</th>
      <th>Date Accessd</th>
    </thead>
    {% for acc in accss_records %}
    <tr>
      <td>{{acc.name}}</td>
      <td>{{acc.date}}</td>
    </tr>
    {% endfor %}        <!-- end for loop -->
  </table>
{% else %}
  <p>No access data</p>
{% endif %}
```

4. edit the template so that its is ready to accept and display the data from the model

5. map the url to the actual view
