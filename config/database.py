from motor.motor_asyncio import AsyncIOMotorClient
import os

# Configuration
ATLAS_PASSWORD = os.environ.get("MONGO_ATLAS_PASSWORD")
ATLAS_USERNAME = os.environ.get("MONGO_ATLAS_USERNAME")

MONGO_URI = "mongodb://localhost:27017/showcomment_db"
DATABASE_NAME = "showcomment_db"

# MongoDB connection setup
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]