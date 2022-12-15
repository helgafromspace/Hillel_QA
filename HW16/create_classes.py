# # Создать классы Employee (сотрудник) и Company (компания).
#
# # Классы должны содержать:
# #
#     # минимум два поля экземпляров и одно поле класса
#     # минимум два метода экземпляра
#     # минимум один метод класса
#     # минимум один статический метод
#     # К методам добавить строки документации.
# #
# # Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
# #
# # Написать код который создает несколько экземпляров и взаимодействует с объектами
# #
# # Задание в том числе и на фантазию
#
from datetime import date, datetime
#
class Company:

    number_of_companies = 0

    def __init__(self, name, year_income, employees_count, foundation_year, status):
        self.name = name
        self.year_income = year_income
        self.employees_count = employees_count
        self.foundation_year = foundation_year
        self.status = status
        Company.number_of_companies += 1

    # считает возраст компании
    def company_age(self):
        now = date.today().year
        return now - self.foundation_year

    # считает средний месячный доход
    def month_avg_income(self):
        return self.year_income // 12

    # измнение статуса с активного на неактивный
    def change_status_to_inactive(self):
        self.status = 'inactive'

    # измнение статуса с неактивного на активный
    def change_status_to_active(self):
        self.status = 'active'

    # изменение значения аттрибута экземпляра: например, чтобы добавив поле для всего класса с помощью функции add_class_attr, изменять значение аттрибута
    # только для экземпляра, оставляя общий таким как есть
    def update_attr(self, attr, value=None):
        if hasattr(self, attr):
            setattr(self, attr, value)
            return f'Attribute \'{self.attr}\' added for {self.name} company with value {value}'
        else:
            return 'Instance doesn\'t have such attribute. Add this attribute to firstly'
    # добавление поля к классу
    @classmethod
    def add_class_attr(cls, attr, value=None):
        if not hasattr(cls, attr):
            setattr(cls, attr, value)
            return f'{attr} attribute is added to class {cls.__name__}'
        else:
            return f'Attribute {attr} exists already'
    # проверка есть ли такой поле в классе
    @classmethod
    def has_attribute(self, attr):
        self.attr = attr
        return hasattr(self, attr)

    # удаление поля класса
    @classmethod
    def del_class_attr(cls, attr):
        delattr(cls, attr)

    @classmethod
    def get_number_of_companies(cls):
        return cls.number_of_companies

    @staticmethod
    # проверяет статус компании
    def is_company_active(company):
        print('Yes') if company.status == 'active' else print('No')

adidas = Company('Adidas', 1200000000, 1000000, 1960, 'active')
nike = Company('Nike', 556000000, 900000, 1950, 'active')
candyshop = Company('CandyTM', 556000, 9000, 1980, 'active')

# проверям есть ли поле 'country' в классе и в экземпляре

print(Company.has_attribute('country'))
print(adidas.has_attribute('country'))

# добавляем поле со значением None в класс и проверяем появилось ли оно в нем и у его экземпляров
print(Company.add_class_attr('country'))
print(Company.country)
print(nike.country)

# пробуем добавить уже существующее поле -  получаем описанное в методе сообщение об ошибке

print(Company.add_class_attr('country'))

# апдейт значения для экземпляра
print(adidas.update_attr('country', 'USA'))

# проверяем, что для поля класса и других экземпляров значение не изменилось
print(Company.country)
print(nike.country)

# удаляем поле класса
Company.del_class_attr('country')

# проверяем, что аттрибут удалился у класса и его экземпляров
print(Company.has_attribute('country'))
print(adidas.has_attribute('country'))
# #
# проверка статуса компании
print(adidas.status)

# изменение статуса и проверка того, что он изменился
adidas.change_status_to_inactive()
print(adidas.status)
adidas.is_company_active(adidas)
candyshop.is_company_active(candyshop)

# считаем возраст компании
print(adidas.company_age())
print(nike.company_age())

# считаем средний месячный доход
print(adidas.month_avg_income())
print(nike.month_avg_income())

# считаем количество созданных компаний
print(Company.get_number_of_companies())
#
class Employee:

    year_salary_raise_value = 1.05

    def __init__(self, name, surname, company, age, salary, job, year_of_start):
        self.name = name
        self.surname = surname
        self.company = company
        self.age = age
        self.salary = salary
        self.job = job
        self.year_of_start = year_of_start

    # распечатка инфо о сотруднике
    def print_info(self):
        print(f'{self.name} {self.surname}: company - {self.company}, age: {self.age}, salary: {self.salary}, job: {self.job}.')

    # получить срок работы работника в компании
    def get_experience_term(self):
        now = date.today().year
        return f'Employee {self.name} {self.surname} has {now - self.year_of_start} years of experience.'

    def get_raised_salary(self):
        raised_salary = round(self.salary * self.year_salary_raise_value)
        return f'Salary increase is {raised_salary - self.salary} $.'

    #
    @classmethod
    def change_raise_value(cls, new_value):
        cls.year_salary_raise_value = new_value
        return new_value

    @staticmethod
    # начало работы
    def start_mark():
        print('Start.')
#
#
#
ann = Employee('Anna', 'Johnes', 'Adidas', 25, 3000, 'SMM', 2019)
josh = Employee('Josh', 'Madsen', 'Nike', 35, 2000, 'Guardian', 2020)

# печатаем инфо о сотруднике
ann.print_info()

# узнаем стаж сотрудника
print(ann.get_experience_term())

# узнаем насколько повысится зп через год при текущем коэффициенте повышения
print(ann.get_raised_salary())

# изменяем коэффициент повышения зп для класса и проверяем изменил ли он значение
print(Employee.year_salary_raise_value)
Employee.change_raise_value(1.1)
print(Employee.year_salary_raise_value)
# на экземпляре класса получаем новое значение повышения зп
print(ann.get_raised_salary())

