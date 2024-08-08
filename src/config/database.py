from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from fastapi import HTTPException
from pymongo.errors import ConnectionFailure
import asyncio
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "commentshow_db"

# MongoDB connection setup
client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi('1'))
db = client[DATABASE_NAME]
connection_status = {"connected": True}

# this function is going to be called by the lifespan function to run when the app launches
async def startup_event():
    
    # the list of tasks are going to run before the sever starts they are going to be async
    tasks = [
        ping_server(),
    ]
    await asyncio.gather(*tasks)
    
# this function checks if the database server is working
async def ping_server():
    try:
        # Attempt to perform a simple operation to check the connection
        await client.admin.command("ping")
        print("Database is up and running")
    except ConnectionFailure as e: 
        raise print(e)

async def simultaneous_function():
    while True:
        print("this is running too!")
        await asyncio.sleep(1)