print('Import module salary.py')

def calculate_salary():
    print('-- The function for calculating_salary has been launched --')

def name_module(text):
    print(text, __name__)

print('End import module salary.py')
print('-' * 40)


if __name__ == '__main__':
    print(__name__)
    print('Start module salary.py')
    calculate_salary()