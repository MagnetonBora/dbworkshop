<<<<<<< HEAD
import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    Date,
)
from sqlalchemy.orm import declarative_base, relationship
=======
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
>>>>>>> 767e6151b0d747c7652e1baf737587a6e3a36ed2


Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

<<<<<<< HEAD
    salaries = relationship("Salary")

    def pay(self, amount, bonus, date=None, comments=None):
        salary = Salary(amount=amount, bonus=bonus)

        if date is not None:
            salary.date = date

        if comments is not None:
            salary.comments = comments

        self.salaries.append(salary)

=======
>>>>>>> 767e6151b0d747c7652e1baf737587a6e3a36ed2
    def __repr__(self):
        return f"Employee({self.id}, {self.first_name}, {self.last_name})"


<<<<<<< HEAD
class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(DECIMAL, nullable=False)
    bonus = Column(DECIMAL, nullable=False, default=0)
    date = Column(
        Date,
        nullable=False,
        default=datetime.date.today
    )
    comments = Column(String(150))

    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    def __repr__(self):
        return f"Salary({self.amount}, {self.date}, {self.employee_id})"


=======
>>>>>>> 767e6151b0d747c7652e1baf737587a6e3a36ed2
class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
<<<<<<< HEAD
        return f"Department({self.id}, {self.name})"
=======
        return f"Department({self.id}, {self.name})"
>>>>>>> 767e6151b0d747c7652e1baf737587a6e3a36ed2
