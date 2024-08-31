from session import Session
from model import Employee, Salary


def main():
    session = Session()

    employee = session.query(Employee).get(1)
    print(employee)

    salary = Salary(
        amount=5000,
        employee_id=employee.id
    )
    session.add(salary)
    session.commit()


if __name__ == "__main__":
    main()