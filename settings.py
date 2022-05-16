# setting the link for DB

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'cnhDb'

# for complete resource
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# for individual items
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

doctor = {
    'item_title': 'doctor',

    # get request for '/doctor/<contactNo>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'contactNo'
    },

    # # most global settings can be overridden at resource level
    # 'resource_methods': ['GET', 'POST'],

    # override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
        },
        'contactNo': {
            'type': 'string',
            'required': True,
            'unique': True
        },
        'rating': {
            'type': 'float',
        },
        'specialization': {
            'type': 'string',
            'required': True
        },
        'degree': {
            'type': 'string',
            'required': True
        }
    }
}

hospital = {
    'item_title': 'hospital',

    # get request for '/hospital/<contactNo>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'contactNo'
    },

    # # most global settings can be overridden at resource level
    # 'resource_methods': ['GET', 'POST'],

    # override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema':{
        'name': {
            'type': 'string',
            'required': True,
            'minlength': 1,
            'maxlength': 100
        },
        'contactNo': {
            'type': 'string',
            'required': True,
            'unique': True
        },
        'noBed': {
            'type':'integer',
            'required': True
        },
        'noIcu': {
            'type': 'integer',
            'required': True
        },
        'location': {
            'type': 'string',
        },
        'rating': {
            'type': 'float',
        }
    }
}

DOMAIN = {
    'doctor': doctor,
    'hospital': hospital
}