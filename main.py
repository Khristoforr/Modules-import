from Modules.application import salary
from Modules.application.db import people
import datetime

if __name__ == '__main__':
    counted_salary = salary.calculate_salary()
    print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
    employee = people.get_employees()
    print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
