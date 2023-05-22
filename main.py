from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(
    title='My api'
)


class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[str] = None


class User(BaseModel):
    user_id: int
    name: str
    subscription: str


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

@app.post('/item')
def post_item(item: Item):
    return item


@app.put('/users')
def put_users(user: User):
    new_id = max(users_db, key=lambda u: u.get('user_id'))['user_id']
    new_user = {
        'user_id': new_id + 1,
        'name': user.name,
        'subscription': user.subscription
    }
    users_db.append(new_user)
    return new_user


@app.post('/users/{userid:int}')
def post_users(user: User, userid):
    try:
        old_user = list(
            filter(lambda x: x.get('user_id') == userid, users_db)
        )[0]

        users_db.remove(old_user)

        old_user['name'] = user.name
        old_user['subscription'] = user.subscription

        users_db.append(old_user)
        return old_user

    except IndexError:
        return {}


@app.delete('/users/{userid:int}')
def delete_users(userid):
    try:
        old_user = list(filter(lambda x: x.get(
            'user_id') == userid, users_db))[0]
        users_db.remove(old_user)
        return {
            'userid': userid,
            'deleted': True
        }
    except IndexError:
        return {}
