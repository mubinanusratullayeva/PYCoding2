# task-1

from datetime import datetime

class Same_infos:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

class Student1(Same_infos):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age)
        self.subject = subject
        self.study_addres = study_addres

class Student2(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student3(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student4(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student5(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student6(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student7(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student8(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student9(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student10(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student11(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student12(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student13(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student14(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)

class Student15(Student1):
    def __init__(self, name, last_name, age, subject, study_addres):
        super().__init__(name, last_name, age, subject, study_addres)


class Group1:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def days_until_end(self):
        current_date = datetime.today()
        end_date = datetime.date.strptime('30-11-2023', '%d-%m-%Y').date()
        return (end_date - current_date).days
student1 = Student1('John', 'Brown', 23, 'Math', 'Harward Universitiy')
student2 = Student2('Jane', 'Smith', '22', 'English', 'Cambridge University')

group_english = Group1('English IELTS', [student1, student2])

print(group_english.days_until_end())