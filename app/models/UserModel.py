import re
from datetime import date
from pydantic import BaseModel, Field, UUID4, EmailStr, field_validator


class UserModel(BaseModel):
    userid: UUID4
    name: str = Field(min_length=0, max_length=50)
    email: EmailStr
    dob: date = Field(
        ge=date(1905,8,1),
        le=date(2026, 12, 31)
    )
    password: str = Field(min_length=8, max_length=32)
    
    
    
    # Function for checking the password formate
    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, value: str) -> str:
        
        # 1. Check for at least one lowercase letter
        if not re.search(r'[a-z]' ,value):
            raise ValueError('Password must contain at least one lowercase letter.')
        
        # 2. Check for at least one uppercase letter
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain at least one uppercase letter.')
        
        # 3. Check for at least one number
        if not re.search(r'[0-9]', value):
            raise ValueError('Password must contain at least one digit.')
            
        # 4. Check for at least one special character
        if not re.search(r'[@$!%*?&]', value):
            raise ValueError('Password must contain at least one special character (@$!%*?&).')
            
        return value
        