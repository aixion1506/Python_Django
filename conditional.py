# # 조건문

# if True:
#     print("True")
# else:
#     print("Fasle")


# if 4 > 3:
#     print("Y")
# else:
#     print("N")

# # input의 입력값을 string 타입으로 처리
# value = input("값 입력: ")

# # # value를 int 정수타입으로 만들어줘야함
# # if int(value) > 5:
# #     print("Y")
# # else:
# #     print("N")

# # 대문자 조건시, 값을 모두 대문자로 처리 필요
# value = value.upper()
# if value == "ENTJ":
#     print("ENTJ")
# else:
#     print("That is not ")


day = input("What is the day today(0~6): ")

if day == "0":
    print("Holiday")
elif day == "6":
    print("Shorted working")
elif day == "1":
    print("Over Working")
else:
    print("Working")