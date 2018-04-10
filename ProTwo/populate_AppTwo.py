import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')
# configuring the settings for the project

import django
django.setup()

## Fake POP script
import random
from AppTwo.models import User
from faker import Faker
fakegeneration = Faker()
def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        # create the fake data for that entry
        fake_firstName = fakegeneration.first_name()
        fake_lastName = fakegeneration.last_name()
        fake_email = fakegeneration.email()

        # create the new User entry
        user = User.objects.get_or_create(first_name=fake_firstName,last_name=fake_lastName,email=fake_email)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")
