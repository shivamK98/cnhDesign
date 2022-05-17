healthPlan = {
    'item_title': 'healthPlan',

    # get request for '/healthPlan/<title>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'title'
    },

    # override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema':{
        'title': {
            'type': 'string',
            'required': True,
            'unique': True,
            'minlength': 1,
            'maxlength': 100
        },
        'price': {
            'type': 'float',
            'required': True
        },
        'description': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1000
        }
    }
}