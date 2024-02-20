# 클래스 - 설계

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

student_1.edit_major('기계공학과')

print(student_1.major)




# student_1_name = student_1.name
# print(student_1_name)


# student_1_graduated = student_1.is_graduated
# print(student_1_graduated)

# student_1.study()