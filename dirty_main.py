from main import *
from application.db.people import *
from application.salary import *


if __name__ == '__main__':
    
    function_call(salary.calculate_salary)
    function_call(people.get_employees)
    function_call(salary.name_module, '-- Module function:')