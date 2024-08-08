from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
import asyncio

# Configuration
ATLAS_PASSWORD = os.environ.get("MONGO_ATLAS_PASSWORD")
ATLAS_USERNAME = os.environ.get("MONGO_ATLAS_USERNAME")

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "commentshow_db"

# MongoDB connection setup
client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi('1'))
db = client[DATABASE_NAME]

async def ping_server():
  # Replace the placeholder with your Atlas connection string
  uri = "mongodb://localhost:27017"
  # Set the Stable API version when creating a new client
  client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
  # Send a ping to confirm a successful connection
  try:
      await client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
      print(e)