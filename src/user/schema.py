'''
maps a user class model to a dictionary. So when a user is retrieved from database we use 
userEntity(user) funtion to normalize the data in a way python understands better 
'''
def userEntity(user) -> dict:
    return{
        "id": str(user["_id"]),
        "email": user["email"],
        "name": user["name"],
        "password": user["password"]
    }