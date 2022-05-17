customer={
    'item_title': 'customer',

    # get request for '/customer/<contactNo>
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
            'required': True,
            'minlength': 1,
            'maxlength': 100
        },
        'email':{
            'type': 'string',
            'unique':True
        },
        'contactNo':{
            'type': 'string',
            'required': True,
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
        }     
    }
}