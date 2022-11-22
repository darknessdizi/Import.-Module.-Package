print('Start module main.py', '*' * 40, sep='\n')

import application.salary as salary
import application.db.people as people
from datetime import datetime
from random_profile import RandomProfile


def function_call(func, arg=None):
    clock = datetime.today().date()
    clock = str(clock)[::-1]
    print(clock)
    if arg == None:
        func()
    else:
        func(arg)

def print_clients(number):

    '''Функция создает случайных клиентов для базы данных'''
    
    clients = RandomProfile()
    
    for i in range(number):
        for i in clients.full_profiles():
            line = f"{i['first_name']} {i['last_name']} {i['gender']} {i['dob']}:"
            print(line)
            print('age:'.ljust(15), i['age'])
            print('phone_number:'.ljust(15), i['phone_number'])
            print('email:'.ljust(15), i['email'])
            print('job_title:'.ljust(15), i['job_title'])
            print('address:'.ljust(15), i['address'], end='\n\n')


print('End module main.py', '*' * 40, sep='\n')


if __name__ == '__main__':

    print('Run:', __name__)

    function_call(salary.calculate_salary)
    function_call(people.get_employees)
    function_call(salary.name_module, '-- Module function:')

    print_clients(5)


    