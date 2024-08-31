from session import Session
<<<<<<< HEAD
from model import Employee, Salary
=======
from model import Employee
>>>>>>> 767e6151b0d747c7652e1baf737587a6e3a36ed2


def main():
    session = Session()

<<<<<<< HEAD
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
=======
    query = session.query(Employee)

    result = query.all()
    print(result)


if __name__ == "__main__":
    main()
>>>>>>> 767e6151b0d747c7652e1baf737587a6e3a36ed2
