from fastapi import FastAPI

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
def welcome():
   return {'data':'Hello, bienvenue sur mon api'}

@app.get('/users')
def get_all_users():
   return users_db

@app.get('/users/{userid:int}')
def get_user_by_id(userid):
   try:
      for user in users_db:
         if user.get('user_id') == userid:
            return user
   except :
      return{}  
   
   
   
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
            return {'Name':user['name']}
   except :
      return{}  
   
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
            return {'Subscription':user['subscription']}
   except :
      return{}  
   
   
# MEILLEURE SOLUTION
#  try:
#         user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
#         return {'subscription': user['subscription']}
#     except IndexError:
#         return {}