from pydantic import BaseModel

class PikachuObject(BaseModel):
    name: str
    is_admin: bool
    age: int

class PikachuResponseObject(BaseModel):
    id: str = ""
    name: str
    is_admin: bool
    age: int
    created_at: str = ""
    updated_at: str = ""
