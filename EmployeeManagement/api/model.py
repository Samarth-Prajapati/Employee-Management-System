from pydantic import BaseModel, EmailStr, StrictBool, StrictStr, StrictFloat
from typing import Optional

class EmployeeModel(BaseModel):
    name: StrictStr
    email: EmailStr
    department: StrictStr
    salary: StrictFloat
    phone_number: StrictStr
    is_active: StrictBool

    class Config:
        orm_mode = True

class EmployeePatchModel(BaseModel):
    is_active: Optional[StrictBool] = True

    class Config:
        orm_mode = True