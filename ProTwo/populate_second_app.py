import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

## Fake Script
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for _ in range(N):
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()
        u = User.objects.get_or_create(first=fake_first, last=fake_last, email=fake_email)[0]
        u.save()
    
if __name__ == "__main__":
    print("populating script!")
    populate(20)
    print("Populating Complete!")