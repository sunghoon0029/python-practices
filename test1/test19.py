# 여러가지 모듈


import calendar
import math
import random
import re
import webbrowser


# print("3.141592")
# print(math.pi)
# calendar.prmonth(2022,10)
# # webbrowser.open("https://naver.com")
# print(random.random() * 11 + 1) # random -> 0 <= answer <1

# # 정규식
# # reg = re.compile("[A-z0-9]{5,15}")
# reg = re.compile("[0-9]{2,3}")
# id = "222"
# print(reg.match(id))
# print(reg.search(id))

# # 회원가입
# # 비밀번호에서 특수문자, 영어 대문자 포함
# # AI 자연어 처리
# # 나는 오늘 좋다

# # 이메일 jo@gmail.com
# reg = re.compile("([A-za-z0-9]+@[A-za-z0-9]+\.[A-za-z]{2,3})")
# print(reg.match("whtjdgns0029@naver.com"))
# # check 정규식

# # 퀴즈
# # 로또 1~45 중복없이 6자리
# 랜덤
# 5줄

# print(random.random() * 11 + 1) # random -> 0 <= answer <1

# numbers = []
# for i in range(0,6):
#     num = random.random() * 45 + 1
#     print(int(num))
   
# lotto = []
# for i in range(0, 5):
#     numbers = []
#     while len(numbers) < 6:
#         num = int(random.random() * 45 + 1)
#         tmpNumber = numbers.copy()
#         tmpNumber.append(num)
#         setNumbers = (numbers.copy())
#         if len(setNumbers) == len(tmpNumber):
#             numbers.append(num)
#     lotto.append(numbers)
# for text in lotto:
#     print(text)

# reg = re.compile("([0-9]+-[0-9]+-[0-9]{3,5})")
# phone_number = "010-2923-6292"
# print(reg.match(phone_number))