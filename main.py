"""
This file is the entry point for the FastAPI application. 
It configures middleware, adds sub-routers, and defines application-level health checks.
"""

from fastapi import APIRouter, FastAPI
from apis import devices, push
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure as needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# List of routers
routers: list[APIRouter] = [devices.router, push.router]

# Add routers to app
for router in routers:
    app.include_router(router)


# Application-Level Health Checks
@app.get("/health")
async def health():
    return {"message": "OK"}


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)