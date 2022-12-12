# Создать классы Employee (сотрудник) и Company (компания).

# Классы должны содержать:
#
    # минимум два поля экземпляров и одно поле класса
    # минимум два метода экземпляра
    # минимум один метод класса
    # минимум один статический метод
    # К методам добавить строки документации.
#
# Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
#
# Написать код который создает несколько экземпляров и взаимодействует с объектами
#
# Задание в том числе и на фантазию

from datetime import date, datetime

class Company:

    status = None

    def __init__(self, name, year_income, employees_count, foundation_year):
        self.name = name
        self.year_income = year_income
        self.employees_count = employees_count
        self.foundation_year = foundation_year

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

    # добавить владельца
    @classmethod
    def add_owner(cls, owner=None):
        cls.owner = owner

    @staticmethod
    # проверяет статус компании
    def is_company_active(company):
        print('Yes') if company.status == 'active' else print('No')

adidas = Company('Adidas', 1200000000, 1000000, 1960)
nike = Company('Nike', 556000000, 900000, 1950)
candyshop = Company('CandyTM', 556000, 9000, 1980)
print(adidas.status)
adidas.change_status_to_inactive()
print(adidas.status)
print(adidas.company_age())
print(nike.company_age())
print(adidas.month_avg_income())
print(nike.month_avg_income())
adidas.add_owner('Dassler')
print(adidas.owner)
nike.add_owner('Bauerman')
print(nike.owner)
adidas.is_company_active(adidas)
candyshop.is_company_active(candyshop)


class Employee:

    hired = None

    def __init__(self, name, surname, company, age, department, job, year_of_start):
        self.name = name
        self.surname = surname
        self.company = company
        self.age = age
        self.department = department
        self.job = job
        self.year_of_start = year_of_start

    # распечатка инфо о сотруднике
    def print_info(self):
        print(f'{self.name} {self.surname}: company - {self.company}, age: {self.age}, department: {self.department}, job: {self.job}.')

    # получить срок работы работника в компании
    def get_experience_term(self):
        if self.hired:
            now = date.today().year
            return f'Employee {self.name} {self.surname} has {now - self.year_of_start} years of experience.'
        else:
            return 'Employee is fired.'

    # проверка нанят ли работник
    def is_person_hired(self):
        if self.hired and self.hired != None:
            print('Yes')
        else:
            print('No')

    # изменение статуса на "нанят"
    @classmethod
    def change_status_to_hired(cls):
        cls.hired = True

    # изменение статуса на "уволен"
    @classmethod
    def change_status_to_fired(cls):
        cls.hired = False

    @staticmethod
    # начало работы
    def start_mark():
        print('Start.')



ann = Employee('Anna', 'Johnes', 'Adidas', 25, 'Marketing', 'SMM', 2019)
josh = Employee('Josh', 'Madsen', 'Nike', 35, 'Security', 'Guardian', 2020)
josh.start_mark()
ann.print_info()
print(ann.get_experience_term())
print(ann.hired)
ann.change_status_to_hired()
print(ann.hired)
ann.is_person_hired()
print(ann.get_experience_term())
josh.change_status_to_hired()
print(josh.hired)
josh.change_status_to_fired()
josh.is_person_hired()