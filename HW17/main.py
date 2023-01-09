from all import Person, Teacher, Student, Grade, Subject


# john = Person('John', 'Doe', 16)
# john.print_info()


sally = Teacher('Sally','Marshall', 45, 'Biology')
joan = Teacher('Joan','Osborne', 35, 'Chemistry')
# joan.print_info()
# print(Teacher.get_list_of_teachers())
# teachers_lst = Teacher.get_list_of_teachers()
# for i in teachers_lst:
#     print(i.__dict__)
#
# biology = Subject('Biology')
# physics = Subject('Physics')
# physics = Subject('Math')
# physics = Subject('Chemistry')
# print(Subject.get_general_list_of_subjects())
#
paul = Student('Paul', 'Johnson', 13, '8A')
# paul.print_info()
paul.add_subject('Biology')
paul.add_subject('Math')
paul.add_subject('Art')
print(paul.get_list_of_subjects())
paul.add_mark('Biology', 'A')
paul.add_mark('Biology', 'B')
paul.add_mark('Math', 'B')
paul.add_mark('Math', 'C')
paul.add_mark('Art', 'A')
# print(paul.get_list_of_marks())
# print(paul.show_grade())
#
sam = Student('Sam', 'Rockwell', 14, '8A')
# sam.print_info()
sam.add_subject('Physics')
sam.add_subject('Chemistry')
# print(sam.get_list_of_subjects())
sam.add_mark('Physics', 'A')
sam.add_mark('Chemistry', 'B')
sam.add_mark('Chemistry', 'B')
sam.add_mark('Physics', 'C')
sam.add_mark('Physics', 'A')
sam.get_list_of_marks()
#
ann = Student('Ann', 'Bennet', 14, '9A')

# print(Student.get_list_of_students())
print(Student.available_marks)
students_list = Student.get_list_of_students()
for i in students_list:
    print(i.__dict__)
# grade_8a = Grade('8A')
# grade_9a = Grade('9A')
# grade_8a.add_student(paul)
# grade_8a.add_student(sam)
# grade_9a.add_student(ann)
# grade_8a.get_list_of_students()
# grade_9a.get_list_of_students()
#