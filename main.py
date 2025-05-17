
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django.setup()
from project_1.models import User, Group

# new_group = Group(name= "вчителі")
# new_group.save()    

# user= User.objects.create(username = "admin"
#                           email = 'admin@gamil.com', role ='admin')

print(User.objects.all())