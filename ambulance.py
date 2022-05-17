ambulance={
    'item_title': 'ambulance',

    # get request for '/ambulance/<vehicleNumber>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'vehicleNumber'
    },

    # override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema':{
        'driverName':{
            'type':'string',
            'required': True,
            'minlength' : 1,
            'maxlength' : 100
        },
        'vehicleNumber':{
            'type':'string',
            'required':True
        },
        'contactNo':{
            'type':'string',
            'required': True
        },
        'availability':{
            'type': 'boolean'
        }
    }
}
