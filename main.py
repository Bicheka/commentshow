from fastapi import FastAPI
from src.user.routes import router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.config.database import startup_event

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run before the app starts
    print("application starting...")
    await startup_event()
    yield
    # Code to run after the app shuts down
    await some_async_function_after()

app = FastAPI(lifespan=lifespan)

async def some_async_function_after():
    
    # TODO Replace this with actual cleanup code if necessary
    print("App is shutting down...")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)