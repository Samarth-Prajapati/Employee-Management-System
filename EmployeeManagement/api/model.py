from pydantic import BaseModel
from typing import Optional

class EmployeeModel(BaseModel):
    name: str
    email: str
    department: str
    salary: float
    phone_number: str
    is_active: bool

    class Config:
        orm_mode = True

class EmployeePatchModel(BaseModel):
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True