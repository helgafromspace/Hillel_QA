from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        '''Method prints info about person'''
        print(f'{self.name}\n{self.surname}\n{self.age}')


class Subject:

    list_of_subjects = []

    def __init__(self, name):
        self.name = name
        Subject.list_of_subjects.append(name)

    @classmethod
    def get_general_list_of_subjects(cls):
        '''Method allows to get list of all available subjects'''
        return cls.list_of_subjects


class Mark:
    def __init__(self, name):
        self.name = name

A = Mark('A')
B = Mark('B')
C = Mark('C')
D = Mark('D')


class Teacher(Person):

    list_of_teachers = []

    def __init__(self, name, surname, age, subject):
        super().__init__(name, age, surname)
        self.subject = subject
        Teacher.list_of_teachers.append((name + ' ' + surname, [subject]))

    def print_info(self):
        print(f'Name: {self.name}\nsurname: {self.surname}\nage: {self.age}\nsubject: {self.subject}')

    @classmethod
    def get_list_of_teachers(cls):
        '''Method allows to get list of teachers'''
        return cls.list_of_teachers


class Student(Person):

    list_of_students = []

    def __init__(self, name, surname, age, grade, list_of_subjects=None, list_of_marks=None):
        super().__init__(name, surname, age)
        self.grade = grade
        self.list_of_subjects = list_of_subjects
        self.list_of_marks = list_of_marks
        Student.list_of_students.append((name, surname))

    def print_info(self):
        print(f'Name: {self.name}\nsurname: {self.surname}\nage: {self.age}\ngrade: {self.grade}')

    def show_grade(self):
        '''Method to show grade of specific student'''
        return f'Student {self.name} {self.surname}is in {self.grade} grade.'

    def add_subject(self, subject):
        '''Method to add subject for student profile'''
        if self.list_of_subjects is None:
            self.list_of_subjects = []
            self.list_of_subjects.append(subject)
        else:
            if subject not in self.list_of_subjects:
                self.list_of_subjects.append(subject)
            else:
                print('This subject is already in list.')

    def get_list_of_subjects(self):
        '''Method allows to get list of subjects'''
        return self.list_of_subjects

    def add_mark(self, subject, mark):
        '''Method to add marks for specific subject for a student'''
        if self.list_of_marks is None:
            self.list_of_marks = {}
            lst = self.get_list_of_subjects()
            for i in lst:
                if i == subject:
                    self.list_of_marks.setdefault(i, []).append(mark.name)
                else:
                    self.list_of_marks.setdefault(i, [])
        else:
            lst = self.get_list_of_subjects()
            for i in lst:
                if i == subject:
                    self.list_of_marks.setdefault(i, []).append(mark.name)
                else:
                    self.list_of_marks.setdefault(i, [])

    def get_list_of_marks(self):
        '''Method to get list of marks'''
        return self.list_of_marks

    @classmethod
    def get_list_of_students(cls):
        '''Method to get list of all students'''
        return cls.list_of_students


class Grade:

    def __init__(self, name, list_of_students=None):
        self.name = name
        self.list_of_students = list_of_students

    def add_student(self, student):
        '''Method to add student to a specific grade'''
        if self.list_of_students is None:
            self.list_of_students = []
            self.list_of_students.append(student)
        else:
            if student not in self.list_of_students:
                self.list_of_students.append(student)
            else:
                print('This student is already in the list.')

    def get_list_of_students(self):
        '''Method to get list of all students of specific grade'''
        print(f'Grade {self.name}: ')
        for i in self.list_of_students:
            print(f'{i.name} {i.surname}, {i.age}')


class AbstractInfo(ABC):

    @abstractmethod
    def print_info(self, *args, **kwargs):
        pass


