from fastapi import FastAPI

api = FastAPI(openapi_tags=[
    {
        'name': 'home',
        'description': 'default functions'
    },
    {
        'name': 'items',
        'description': 'functions that are used to deal with items'
    }
])


@api.get('/', tags=['home'])
def get_index():
    """returns greetings
    """
    return {
        'greetings': 'hello world'
    }


@api.get('/items', tags=['home', 'items'])
def get_items():
    """returns an item
    """
    return {
        'item': "some item"
    }
