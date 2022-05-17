doctor = {
    'item_title': 'doctor',

    # get request for '/doctor/<contactNo>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'contactNo'
    },

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