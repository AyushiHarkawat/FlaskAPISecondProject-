from werkzeug.security import safe_str_cmp
from user import User

# users =[
#     {
#         'id':1,
#         'username': 'bob',
#         'password':'asdf'
#     }
# ]

users = [
    User(1, 'bob', 'asdf')
]

# user_mapping = { 'bob': {
#         'id':1,
#         'username': 'bob',
#         'password':'asdf'
#     }
# }
user_mapping = {u.username:u for u in users}

# userid_mapping = { 1: {
#         'id':1,
#         'username': 'bob',
#         'password':'asdf'
#     }
# }

userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = user_mapping.get(username, None)
    # if user and user.password == password:
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
