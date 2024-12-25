from datetime import datetime
from core.economy import services, items
from core.database import users # users collection 
import core.terminal as console
from core.users import badges, connections, badges
from pydantic import BaseModel, Field

class User(BaseModel):
    user_id: int = Field(default=None)
    server_id: int = Field(default=None)
    active: datetime = Field(default=datetime.now())
    energy: float = Field(default=100.000)
    terminal: dict = Field(default={"mode": "g"})
    profile: dict = Field(default={
        "name": str,
        "pfp": str,
        "bio": "Hello,\nI just registered my account here. Lets get started with a lot of fun activities though this bot.\nThank you",
        "views": 0,
        "followers": [],
        "flist": [],
        "badges": [],
        "rating": (0, 0),
    })
    requests: dict = Field(default={"count": 0, "content": []})
    economy: dict = Field(default={
        "money": {"wallet": 99, "bank": 0},
        "services": {"default": {}, "custom": {}},
        "items": {"default": {}, "custom": {}},
        "jobs": {"default": {}, "custom": {}},
    })

    