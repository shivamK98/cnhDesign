login={
    'item_title': 'login',

    # get request for '/login/<userId>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'userId'
    },

    # override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': {
        'role': {
            'type': 'string',
            'required': True,
            'minlength': 1,
            'maxlength': 50
        },
        'userId': {
            'type': 'objectid',
            'required': True
        },
        'email': {
            'type': 'string',
            'required': True,
            'unique': True
        },
        'password': {
            'type': 'string',
            'required': True

        }
    }
}