# 대, 소문자화
city = "seoul"
print(city)

city.upper()
print(city.upper())

city = city.upper()
print(city)


city.lower()
print(city.lower())


city = city.lower()
print(city)



# strip()사용시 양쪽 공백 제거
occupation = "   developer"
print(occupation)

occupation.lstrip()
print(occupation.strip())


# 줄 띄어쓰기 '\n'사용
print("vv\nvv\nnn")


# .removeprefix 사용시 끝쪽 글자 제거 후 출력 가능
score = "점수:90"
print(score.removeprefix("점수:"))

# .removesuffix 사용시 앞쪽 글자 제거 후 출력 가능
score_2 = "80점"
print(score_2.removesuffix("점"))

# 특정 단어 대치
city = "서울 중구"
print(city.replace("서울", "서울시"))

# 특정 단어에 추가해 가공
si_1 = "용인"
gu_1 = "기흥"
address_1 = f"{si_1}시 {gu_1}구"
print(address_1)

si_2 = "서울"
gu_2 = "종로"
address_2 = f"{si_2}시 {gu_2}구"
print(address_2)


