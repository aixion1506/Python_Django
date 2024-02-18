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

colors = ['red', 'green', 'blue']

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

colors.remove('blue')
print(colors)