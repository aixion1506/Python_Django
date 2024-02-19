# 딕셔너리

student = {
    "student_no" : "202301234",
    "major" : "English",
    "grade" : 1
}

print(student["student_no"])

# student딕셔너리의 요소 변경
student["student_no"] = "20230987"

print(student)
print(student["student_no"])


# 새로운 요소 추가
student["gpa"] = 4.5
print(student)

# 기존 요소 수정
student["gpa"] = 4.0
print(student)

# 기존 요소 삭제
del student["grade"]
print(student)

# 데이터 접근 및 미발견시
print(student.get("vvs", "해당 키-값 쌍이 존재하지 않음"))

# 딕셔너리 키 반환
print(list(student.keys()))

# 딕셔너리 값 반환
print(list(student.values()))