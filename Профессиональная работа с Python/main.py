from applecation import  salary
from applecation.db import  people
from datetime import date
if __name__ == '__main__':
    now_date = date.today()
    print(now_date)
    one = salary
    print(one.calculate_salary())
    two= people
    print(two.get_employees())