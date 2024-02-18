# 튜플
"""
튜플은 요소 일부를 바꾸는건 불가능
하지만 튜플 자체를 통째로 재선언은 가능
"""


tup = (1, 20, 40)
# print(tup[0])


# tup = (100, 30, 4)
# print(tup)

# # 요소를 하나씩 추출
# for x in tup:
#     print(x)


# 리스트로 변환1, 파이썬 내장함수 `list`
list_1 = list(tup)
print(list_1)

# 리스트로 변환2, 리스트에 요소를 하나씩 넣기(리스트 컴프리헨션)
list_2 = [x for x in tup]
print(list_2)

# 리스트로 변환3, 반복문과 append메서드 사용으로 추가
list_3 = []

for x in tup:
    list_3.append(x)
print(list_3)
