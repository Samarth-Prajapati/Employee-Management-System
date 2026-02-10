from EmployeeManagement.database import create_tables, get_db, Employee
from EmployeeManagement.api.model import EmployeeModel, EmployeePatchModel
from EmployeeManagement.api.validator import check_contact, check_salary
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
app = FastAPI()

if not create_tables():
    create_tables()

@app.get("/")
def index():
    return {"message": "Welcome to Employee Management System"}

@app.get("/employees", status_code = status.HTTP_200_OK, tags = ["Employees"])
def fetch_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

@app.get("/employees/{employee_id}", status_code = status.HTTP_200_OK, tags = ["Employees"])
def fetch_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Employee not found")
    else:
        return employee

@app.post("/employees", status_code = status.HTTP_201_CREATED, tags = ["Employees"])
def add_employee(request: EmployeeModel, db: Session = Depends(get_db)):
    if not check_contact(request.phone_number):
        raise HTTPException(status_code = 400, detail = "Invalid Phone Number")
    if not check_salary(request.salary):
        raise HTTPException(status_code = 400, detail = "Invalid Salary")
    employee = Employee(name = request.name, email = request.email, department = request.department, salary = request.salary, phone_number = request.phone_number, is_active = request.is_active)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

@app.put("/employees/{employee_id}", status_code = status.HTTP_202_ACCEPTED, tags = ["Employees"])
def update_employee(employee_id: int, request: EmployeeModel, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Employee not found")
    employee.name = request.name
    employee.email = request.email
    employee.department = request.department
    if not check_salary(request.salary):
        raise HTTPException(status_code = 400, detail = "Invalid Salary")
    employee.salary = request.salary
    if not check_contact(request.phone_number):
        raise HTTPException(status_code = 400, detail = "Invalid Phone Number")
    employee.phone_number = request.phone_number
    employee.is_active = request.is_active
    db.commit()
    db.refresh(employee)
    return employee

@app.patch("/employees/{employee_id}/status", status_code = status.HTTP_202_ACCEPTED, tags = ["Employees"])
def partial_update_employee(employee_id: int, request: EmployeePatchModel, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Employee not found")
    employee.is_active = request.is_active
    employee.name = employee.name
    employee.email = employee.email
    employee.department = employee.department
    employee.salary = employee.salary
    employee.phone_number = employee.phone_number
    db.commit()
    db.refresh(employee)
    return employee

@app.delete("/employees/{employee_id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["Employees"])
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Employee not found")
    db.delete(employee)
    db.commit()
    return f"Employee with id - {employee_id} has been removed successfully."