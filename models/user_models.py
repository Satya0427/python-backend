# models/user_models.py

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from datetime import date

class StatusResponse(BaseModel):
    sts: str
    msg: str

class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    dob: Optional[date] = None
    created_at: Optional[date] = None # Make optional if it might be null
    # We will send the image as a Base64 encoded string.
    profilePic: Optional[str] = None

class UserListResponse:
    status: StatusResponse
    data: Optional[List[User]] = []

class userLogins(BaseModel):
    email:EmailStr
    password:str