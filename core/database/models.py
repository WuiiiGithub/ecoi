from __future__ import annotations
from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import re

# Utility function for age validation
def calculate_age(dob: datetime) -> int:
    today = datetime.now()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Terminal Schema
class TerminalSchema(BaseModel):
    mode: str = Field(..., description="Mode for terminal - g for global, s for server, u for user level")
    
    @field_validator('mode')
    def validate_mode(cls, value):
        if value not in ['g', 's', 'u']:
            raise ValueError("Mode must be one of 'g', 's', or 'u'")
        return value

# Profile Schema
class ProfileSchema(BaseModel):
    name: str
    pfp: str  # Profile picture URL
    bio: str = Field(default="Hello,\nI just registered my account here. Let's get started with a lot of fun activities through this bot.\nThank you")
    views: int = 0
    followers: List[int] = []
    flist: List[int] = []  # Friend list
    badges: List[str] = []
    rating: Tuple[int, int] = (0, 0)  # (rating, total ratings count)
    dob: Optional[datetime] = None  # Date of Birth for age validation
    gender: Optional[str] = None  # Gender
    location: Optional[str] = None  # Location (optional)
    
    @field_validator('name')
    def validate_name_length(cls, value):
        if len(value) < 3 or len(value) > 50:
            raise ValueError("Name must be between 3 and 50 characters.")
        return value
    
    @field_validator('bio')
    def validate_bio_length(cls, value):
        if len(value) < 10 or len(value) > 500:
            raise ValueError("Bio must be between 10 and 500 characters.")
        return value
    
    @field_validator('views')
    def validate_views(cls, value):
        if value < 0:
            raise ValueError("Views cannot be negative")
        return value

    @field_validator('followers', 'flist')
    def validate_unique_ids(cls, value):
        if len(value) != len(set(value)):
            raise ValueError("Followers and Friend list cannot have duplicate user IDs.")
        return value

    @field_validator('rating')
    def validate_rating(cls, value):
        if value[0] < 0 or value[1] <= 0:
            raise ValueError("Invalid rating tuple. Rating cannot be negative, and total count must be positive.")
        return value
    
    @model_validator(mode='before')
    def validate_age(cls, values):
        # Ensure user is above 18 years old
        if 'dob' in values and values['dob']:
            age = calculate_age(values['dob'])
            if age < 18:
                raise ValueError("User must be at least 18 years old.")
        return values


# Badge Schema
class BadgeSchema(BaseModel):
    name: str
    description: str
    emoji: str
    since: datetime
    expires: Optional[datetime] = None
    
    @field_validator('expires', always=True)
    def validate_expiry(cls, value, values):
        if value and values.get('since') and value < values['since']:
            raise ValueError("Expiry date cannot be earlier than the 'since' date.")
        return value

# Bio Schema (Refactor to include personality, skills, etc.)
class BioSchema(BaseModel):
    personality: Dict[str, str]  # e.g. temperament, presence, zodiac, mbti
    description: str
    interests: List[Dict[str, str]]  # [{name, link, description}]
    skills: List[Dict[str, str]]  # [{name, proofs: [{name, link, description, date}]}]
    projects: List[Dict[str, str]]  # [{name, link, description, date}]
    education: List[Dict[str, str]]  # [{name, link, description, since, till}]

    @model_validator(mode='before')
    def validate_bio(cls, values):
        if not values.get('interests') or not values.get('skills') or not values.get('projects'):
            raise ValueError("Bio must include at least one interest, skill, and project.")
        return values

# Connections Schema
class ConnectionsSchema(BaseModel):
    followers: Dict[int, Dict[str, datetime]]  # {userID: {"since": datetime, "intimacy": float}, ...}
    following: Dict[int, Dict[str, datetime]]  # {userID: {"since": datetime, "intimacy": float}, ...}
    blocked: Dict[int, datetime]  # {userID: datetime, ...}
    amtFollowers: int = 0
    amtFollowing: int = 0
    amtBlocked: int = 0
    
    @model_validator(mode='before')
    def validate_connections(cls, values: dict) -> dict:
        followers = values.get('followers', {})
        following = values.get('following', {})
        blocked = values.get('blocked', {})

        if any(user_id in following for user_id in followers):
            raise ValueError("A user cannot be both a follower and following another user.")
        if any(user_id in following for user_id in blocked):
            raise ValueError("A user cannot be both blocked and following another user.")
        if values.get('amtFollowers') != len(followers):
            raise ValueError("amtFollowers count must match the number of followers.")
        if values.get('amtFollowing') != len(following):
            raise ValueError("amtFollowing count must match the number of following.")
        if values.get('amtBlocked') != len(blocked):
            raise ValueError("amtBlocked count must match the number of blocked users.")
        return values

# Economy Schema
class EconomySchema(BaseModel):
    money: Dict[str, int] = Field(default={"wallet": 99, "bank": 0})
    services: Dict[str, Dict] = Field(default={"default": {}, "custom": {}})
    items: Dict[str, Dict] = Field(default={"default": {}, "custom": {}})
    jobs: Dict[str, Dict] = Field(default={"default": {}, "custom": {}})
    
    @model_validator(mode='before')
    def validate_money(cls, values):
        money = values.get('money', {})
        if any(amount < 0 for amount in money.values()):
            raise ValueError("Money values cannot be negative.")
        return values

# Requests Schema
class RequestsSchema(BaseModel):
    count: int = 0
    content: List[Dict[str, str]] = []

    @field_validator('content')
    def validate_requests(cls, value):
        if len(value) > 50:
            raise ValueError("Too many requests.")
        return value
    
# User Schema
class UserSchema(BaseModel):
    user_id: int
    gmail: Optional[EmailStr] = None  # Email validation with EmailStr
    server_id: Optional[int] = None
    active: datetime = Field(default=datetime.now())
    energy: float = Field(default=100.0)
    terminal: TerminalSchema = Field(default_factory=TerminalSchema)
    profile: ProfileSchema = Field(default_factory=ProfileSchema)  # Profile contains bio, name, age, etc.
    requests: Dict = Field(default={"count": 0, "content": []})
    economy: EconomySchema = Field(default_factory=EconomySchema)
    connections: ConnectionsSchema = Field(default_factory=ConnectionsSchema)

    @field_validator('gmail')
    def validate_gmail(cls, value: str) -> str:
        if value and not value.endswith('@gmail.com'):
            raise ValueError("Gmail must end with '@gmail.com'")
        return value

    @model_validator(mode='before')
    def validate_user_data(cls, values):
        # Age validation: Ensure user is above 18
        if values.get('energy', 100) < 0 or values.get('energy', 100) > 100:
            raise ValueError("Energy must be between 0 and 100.")
        return values
