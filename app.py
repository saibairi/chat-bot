from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller import chatboot_controller

app = FastAPI()

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(chatboot_controller.router,prefix="/chat-bot")
