from pydantic import BaseModel,EmailStr

class userLogins(BaseModel):
    email:EmailStr
    password:str