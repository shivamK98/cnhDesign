hospital = {
    'item_title': 'hospital',

    # get request for '/hospital/<contactNo>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'contactNo'
    },

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
        'address': {
            'type': 'dict',
            'schema':{
                'line1':{
                    'type':'string',
                    'minlength': 1,
                    'maxlength': 150
                },
                'city':{
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 30,
                    'required': True
                },
                'state':{
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 30,
                    'required': True
                },
                'pincode': {
                    'type': 'number',
                    'maxlength':6,
                    'required': True 
                }
            },  
        },
        'rating': {
            'type': 'float',
        }
    }
}