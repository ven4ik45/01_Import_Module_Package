import datetime

from application.db.people import get_employees
from application.salary import calculate_salary


def get_date():
    print(datetime.date.today())

if __name__ == '__main__':
    get_date()
    print(calculate_salary())
    print(get_employees())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
