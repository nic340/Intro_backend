from sqlmodel import Session, select
from database import engine
from models import Employee, Department, Project

# ------------------------
# Employee CRUD
# ------------------------
def create_employee(name: str, dept: int, age: int = None):
    with Session(engine) as session:
        emp = Employee(name=name, dept=dept, age=age)
        session.add(emp)
        session.commit()
        session.refresh(emp)
        return emp

def get_employee(empid: int):
    with Session(engine) as session:
        return session.get(Employee, empid)

def get_all_employees():
    with Session(engine) as session:
        return session.exec(select(Employee)).all()

def delete_employee(empid: int):
    with Session(engine) as session:
        emp = session.get(Employee, empid)
        if emp:
            session.delete(emp)
            session.commit()
            return True
        return False

# ------------------------
# Department CRUD
# ------------------------
def create_department(name: str):
    with Session(engine) as session:
        dept = Department(name=name)
        session.add(dept)
        session.commit()
        session.refresh(dept)
        return dept

def get_department(dept_id: int):
    with Session(engine) as session:
        return session.get(Department, dept_id)

def get_all_departments():
    with Session(engine) as session:
        return session.exec(select(Department)).all()

def delete_department(dept_id: int):
    with Session(engine) as session:
        dept = session.get(Department, dept_id)
        if dept:
            session.delete(dept)
            session.commit()
            return True
        return False

# ------------------------
# Project CRUD (new)
# ------------------------
def create_project(title: str, description: str, owner_id: int):
    with Session(engine) as session:
        proj = Project(title=title, description=description, owner_id=owner_id)
        session.add(proj)
        session.commit()
        session.refresh(proj)
        return proj

def get_project(project_id: int):
    with Session(engine) as session:
        return session.get(Project, project_id)

def get_all_projects():
    with Session(engine) as session:
        return session.exec(select(Project)).all()

def delete_project(project_id: int):
    with Session(engine) as session:
        proj = session.get(Project, project_id)
        if proj:
            session.delete(proj)
            session.commit()
            return True
        return False