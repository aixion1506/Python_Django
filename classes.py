"""
객체지향 - 설계
""" 
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        # 졸업 여부는 기본적으로 False설정시 인자 처리 안함
        self.is_graduated = False

    def study(self):
        print(f'{self.name} 학생은 공부 중입니다.')

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f'{student_1.major}로 전공이 변경되었습니다.')


# 인스턴스 - 실체화된 사물

student_1 = Student('라니안', '컴공과')

# student_1.edit_major('기계공학과')

# print(student_1.major)




# student_1_name = student_1.name
# print(student_1_name)


# student_1_graduated = student_1.is_graduated
# print(student_1_graduated)

# student_1.study()



"""
객체지향 - 상속
"""

class ForeignStudent(Student):
    def __init__(self, name, major, country):
        #  `super()`는 기존 부모 클래스의 인자를 계승
        super().__init__(name, major)
        #  `ForeignStudent`클래스만의 새로운 인자를 self로 선언
        self.country = country

    # 오버라이딩
    # 부모클래스의 함수를 가져와 자식클래스에서 수정해 사용하는것
    def study(self):
        print(f'{self.name} is studying now')

foreign_stud_1 = ForeignStudent('라니학교', '고양이과', '라니랜드')
print(foreign_stud_1.name)
print(foreign_stud_1.major)
print(foreign_stud_1.is_graduated)
print(foreign_stud_1.country)

foreign_stud_1.study()