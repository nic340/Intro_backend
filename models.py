from typing import Optional
from sqlmodel import SQLModel, Field

# ------------------------
# Employee Model
# ------------------------
class Employee(SQLModel, table=True):
    empid: Optional[int] = Field(default=None, primary_key=True)
    name: str
    dept: Optional[int] = Field(default=None, foreign_key="department.id")
    age: Optional[int] = None

# ------------------------
# Department Model
# ------------------------
class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

# ------------------------
# Project Model (new)
# ------------------------
class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    owner_id: int = Field(foreign_key="employee.empid")