# # 리스트(lists)

# mbti = ['ENFP', 'ENTP', 'ENTJ', 'INTP']

# print(mbti)
# print(mbti[0])

# # 배열 내용도 재선언시 변경 가능
# mbti[0] = 'INFP'
# print(mbti[0])

# # 배열의 내용의 타입이 달라도 선언 자체는 가능
# # 이후 처리할때는 조심해야함
# my_list = [123, 'apple']
# print(my_list)

# colors = ['red', 'green', 'blue']

# colors[2] = 'black'
# print(colors)

# # 마지막에 새로 추가하는 메서드
# colors.append('purple')
# print(colors)

# # 특정 지점에 추가하는 메서드
# colors.insert(1, 'yellow')
# print(colors)

# # 특정 지점 제거
# del colors[0]
# print(colors)

# # 특정 지점 제외 제거
# color = colors.pop(0)
# print(color)

# colors.remove('blue')
# print(colors)


# colors = ['red', 'green', 'gray', 'black', 'yellow', 'blue']

# # 오름차순 정렬
# colors.sort()
# print(colors)
# print(sorted(colors))


# # 내림차순 정렬
# colors.sort(reverse=True)
# print(colors)



# # 길이 - 요소의 개수
# print(len(colors))

# # 리스트의 마지막 값 확인
# print(colors[-1])



# colors = ['red', 'green', 'gray', 'black', 'yellow', 'blue']

# # 원본 데이터의 왜곡방지로 다른변수에 할당
# color_2 = colors[:]
# print(color_2)

# # `a:b` 리스트내 a에서 b까지
# # print(colors[1:6])

# # `:a` 리스트내 a까지
# print(colors[:4])

# # `a:` 리스트내 a부터
# # print(colors[2:])

# # `-1:` 리스트내 뒤에서부터 첫번째
# # print(colors[-1:])



scores = [11, 22, 77, 33, 44, 55]

# reverse 옵션에 따른 오름,내림차순 정렬
# scores.sort(reverse=True)
# print(scores)

# # in 뒤의 scores의 요소들인 score를 하나하나 정렬
# for score in scores:
#     print(score)


# # 40이상의 수를 출력, 그 외는 실패로 설정
# for score in scores:
#     if score >= 40:    
#         print(score)
#     else:
#         print("Fail")

# 리스트의 최대, 최소, 총합 정렬

# max_val = max(scores)
# min_val = min(scores)

# # 파이썬 내부 함수 `sum`을 이용한 총합 
# sum_val = sum(scores)
# print(sum_val)

# # sum이라는 결과를 만든 조건문을 이용한 총합
# sum_values = 0
# for score in scores:
#     sum_values = sum_values+score
# print(sum_values)

# 평균값 출력
avg_val = sum(scores) / len(scores)
print(avg_val)