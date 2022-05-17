testimonial={
    'item_title': 'testimonial',

    # get request for '/testimonial/<customerId>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'customerId'
    },

    # override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': {
        'text':{
            'type': 'string',
            'minlength': 1,
            'maxlength': 1000,
        },
        'customerId':{
            'type': 'string',
            'required': True
        },
        'doctorId':{
            'type': 'string'
        },
        'hospitalId':{
            'type': 'string'
        }
    }
}