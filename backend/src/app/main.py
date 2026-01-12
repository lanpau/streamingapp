import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    debug=settings.debug
)

# CORS Configuration
# WARN: This is too permissive for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from app.api.v1.streams import router as streams_router

app.include_router(streams_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {
        "message": settings.app_name,
        "docs": "/docs",
        "version": "0.1.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "version": "0.1.0"
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )
