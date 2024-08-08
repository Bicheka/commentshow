from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import asyncio
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "commentshow_db"

# MongoDB connection setup
client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi('1'))
db = client[DATABASE_NAME]
connection_status = {"connected": True}

# this function is going to be called by the lifespan function to run when the app launches
async def startup_event():
    # Start the background task to monitor the connection
    try:
        asyncio.create_task(ping_server())
        print("Successfully connected to database!")
    except:
        print("Could not connect to database")
    
# this function is going to check the satus of the database every x amount of time
async def ping_server():
    while True:
        try:
            await client.admin.command('ping')
            connection_status["connected"] = True
            print("db status: connected")
        except:
            connection_status["connected"] = False
            print("db status: disconnected")
        await asyncio.sleep(10)  # Ping every 10 seconds