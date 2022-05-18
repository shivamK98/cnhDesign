order={
    'item_title': 'order',

    # get request for '/order/<customerId>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'customerId'
    },

    # override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema':{
        'customerId': {
            'type': 'objectid',
            'required': True,
            'unique': True,
        },
        # 'dateTime': {
        #       available as '_created' and '_updated' by default
        # }

        'plan':{
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'planId': {
                        'type' : 'objectid',
                        'required' : True,
                        'unique': True 
                    },
                    'price': {
                        'type': 'float',
                        'required': True
                    }
                },
            }
        }
    }
}