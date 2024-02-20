# # 정수를 0으로 나누는 경우
# a = 10
# b = 0

# a / b
# 리스트를 초과하는 값인 경우
fruits = ['apple', 'banana', 'strawberry']

# 예외가 있을 수 있는 코드는 try에서 처리
# fruits[3]을 조건으로
try:
    fruits[3]
# 예외시 출력
except:
    print('인덱스 참고 불가')
# 정상 출력시 출력
else:
    print('정상 수행')