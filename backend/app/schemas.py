from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    refresh_token: str  # Include refresh token here
    token_type: str = "bearer"  # Default to 'bearer'


class TokenData(BaseModel):
    username: str | None = None


class LoginRequest(BaseModel):
    username: str
    password: str


class GroupChatResponse(BaseModel):
    group_name: str

    class Config:
        orm_mode = True  # Enables FastAPI to work with ORM models like SQLAlchemy


class GroupChatRequest(BaseModel):
    group_name: str
    admin_username: str
