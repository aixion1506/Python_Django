# from classes import Student, ForeignStudent
# 클래스 페이지의 모든 함수를 가져옴
from classes import *

stud_1 =  Student('라니안', '컴공과')
foreign_stud_1 = ForeignStudent('라니학교', '고양이과', '라니랜드')

stud_1.study()
foreign_stud_1.study()