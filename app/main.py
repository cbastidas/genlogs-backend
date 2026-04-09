from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

# Initialize the FastAPI app
app = FastAPI(
    title="Genlogs Carrier API",
    description="Returns carriers operating between two cities",
    version="1.0.0",
)

# CORS — allows the React frontend to call this API from the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace * with your Vercel URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(router)


@app.get("/")
def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "Genlogs Carrier API is running"}