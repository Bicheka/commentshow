from config import database
from fastapi import HTTPException, status
from .model import User
from .encryption import encrypt_password

USER_COLLECTION = "user"
collection = database.db[USER_COLLECTION]

async def create_user(user: User):
    print(database.client.address)
    # Check if the user already exists
    existing_user = await collection.find_one({"email":user.email})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered")
    
    # Hash the user's password
    hashed_password = encrypt_password(user.password)
    user.password = hashed_password
    try:
        print(user)
        await collection.insert_one(dict(user))
    except: 
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection to db error")