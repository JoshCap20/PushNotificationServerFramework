from fastapi import FastAPI
from apis import devices
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
routers: list[FastAPI.router] = [devices.router]

for router in routers:
    app.include_router(router)


# Application-Level Health Checks
@app.get("/health")
async def health():
    return {"message": "OK"}


@app.get("/")
async def root():
    return {"message": "Hello World"}
