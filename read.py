import django
import csv
#from django.core.management import setup_environ
from restaurant import settings
#setup_environ(settings)
import sys,os
from django.core.wsgi import get_wsgi_application
#sys.path.append()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant.settings")
django.setup()
application = get_wsgi_application()
from resapp.models import *
with open("data.csv") as f:
       reader = csv.reader(f,delimiter=',')
       rows = list(reader)
       for row in range(192):
           _, created = RestaurantModel.objects.get_or_create(
               name = rows[row][0],
               url = rows[row][1],
               city = rows[row][3],
               address = rows[row][2],
               )
