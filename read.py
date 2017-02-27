import django
django.setup()
import csv
from resapp.models import *
import sys,os
from django.core.wsgi import get_wsgi_application
#sys.path.append()
os.environ['DJANGO_SETTINGS_MODULE'] = 'restaurant.settings'
application = get_wsgi_application()

with open("data.csv") as f:
       reader = csv.reader(f,delimiter=',')
       rows = list(reader)
       for row in range(3):
           _, created = RestaurantModel.objects.get_or_create(
               name = rows[row][0],
               url = rows[row][1],
               city = rows[row][3],
               address = rows[row][2],
               )
