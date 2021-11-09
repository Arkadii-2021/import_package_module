from salary import calculate_salary
from db.people import get_employees
import datetime

now = datetime.datetime.now()
today_date = now.strftime("%d.%m.%Y")
print(f'Сегодня: {today_date} \n')

if __name__ == '__main__':
    calculate_salary()
    get_employees()
