import imp
from doctor import doctor
from hospital import hospital
from ambulance import ambulance
from customer import customer
from testimonial import testimonial
from healthPlan import healthPlan
from order import order
from login import login

# setting the link for DB
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'cnhDb'

# for complete resource
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# for individual items
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# all mongoDb databases
DOMAIN = {
    'doctor': doctor,
    'hospital': hospital,
    'ambulance': ambulance,
    'customer': customer,
    'testimonial': testimonial,
    'healthPlan': healthPlan,
    'order': order,
    'login': login
}
