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
