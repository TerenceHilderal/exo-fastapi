from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title='My api'
)

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]


@app.get('/')
def get_index(argument1):
    return {
        'data': argument1
    }


@app.get('/typed')
def get_typed(argument1: int):
    return {
        'data': argument1 + 1
    }


@app.get('/addition')
def get_addition(a: int, b: Optional[int] = None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {
        'addition_result': result
    }


@app.get('/users')
def get_all_users():
    return users_db


@app.get('/users/{userid:int}')
def get_user_by_id(userid):
    try:
        for user in users_db:
            if user.get('user_id') == userid:
                return user
    except:
        return {}

        # MEILLEURE SOLUTION

    # try:
    #    user = list(filter(lambda x: x.get('user_id')==userid,users_db))[0]
    #    return user
    # except IndexError:
    #    return{}


@app.get('/users/{userid:int}/name')
def get_user_name(userid):
    try:
        for user in users_db:
            if user.get('user_id') == userid:
                return {'Name': user['name']}
    except:
        return {}

        # MEILLEURE SOLUTION
    #  try:
    #      user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
    #      return {'name': user['name']}
    #  except IndexError:
    #      return {}


@app.get('/users/{userid:int}/subscription')
def get_subscription(userid):
    try:
        for user in users_db:
            if user.get('user_id') == userid:
                return {'Subscription': user['subscription']}
    except:
        return {}


# MEILLEURE SOLUTION
#  try:
#         user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
#         return {'subscription': user['subscription']}
#     except IndexError:
#         return {}
