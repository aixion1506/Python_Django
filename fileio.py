"""
파일 읽기
"""

# # 파일 읽기모드
# f = open ('./literature/poem.txt', 'r', encoding = ' UTF-8')
# # 파일 읽기
# print(f.read())
# print(f.readline())
# # 파일 닫기
# f.close()

# # with open시 추가적으로 close() 작업 xx
# with open('./literature/poem.txt', 'r', encoding = 'UTF-8') as f:
#     print(f.read())


"""
파일 쓰기
"""
# 파일 쓰기모드
# w : 모든 글 초기화후 입력 / a : 기존 글 유지후 작성
f = open ('./literature/poem2.txt', 'a', encoding = 'UTF-8')

f.write('\n새로운 글이 작성되었습니다.')

f.close