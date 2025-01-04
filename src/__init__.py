from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.config.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting")
    yield
    print("server is shutting down")

app = FastAPI()

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    lifespan=lifespan
)
origins = [
    settings.FRONTEND_ORIGIN,  # Allow your frontend's origin
    # Add other origins if needed
]

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Adjust for your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
