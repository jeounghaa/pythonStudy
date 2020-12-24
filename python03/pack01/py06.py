# 1. 첫줄에는 별 1개부터 시작하여 10번째 줄에는 별 10개가 찍히게
# for i in range(0, 10):
#     for j in range(0, i+1):
#         print('*', end='')
#     print()

# 2. 나의 이름: 홍길동
#    나의 나이: 100
#    나의 성별: 남
#    나의 좌우명: 열심히 살자
# -------------------------
# 나는 홍길동이고, 내 나이는 100세
# 내년 나이는 101세가 될 예정이고,
# 나는 남, 나는 열심히 살자!가 내 좌우명

# name = input('나의 이름: ')
# age = input('나의 나이: ')
# gender = input('나의 성별: ')
# motto = input('나의 좌우명: ')
#
# print('나는 %s, 나이는 %d, 내년 나이는 %d, 성별은 %s, 좌우명은 %s' % (name, int(age), int(age)+1, gender, motto))


# 3. 콘솔에서 당신의 이름을 입력, 콘솔에서 당신이 관심사를 입력
# 메세지 박스로 이름과 관심사를 출력
# 관심사가 파이썬이라면 '분석가가 되실 거군'
# 아니라면 '개발자가 되실거군'

# from tkinter import messagebox
#
# name = input('이름>> ')
# interest = input('관심사>> ')
# if(interest == '파이썬'):
#     result = '분석가'
# else:
#     result = '개발자'
#
# messagebox.showinfo(message=result + '가 되실거군')


# 4. 1) 오늘 날짜와 시각을 datetime라이브러리를 이용해 찍으세요
#    2) 3-5월이면 봄, 6-8이면 여름, 9-11이면 가을, 나머지는 가을
# from datetime import datetime
#
# print('오늘 날짜와 시각: ' + str(datetime.now()))
#
# if 3 <= datetime.now().month <= 5:
#     print('봄')
# elif 6 <= datetime.now().month <= 8:
#     print('여름')
# elif 9 <= datetime.now().month <= 11:
#     print('가을')
# else:
#     print('겨울')


# 5. 55부터 688까지 3씩 점프하면서 모두 더해보세요.
# sum = 0
#
# for i in range(55, 689, 3):
#     print(i)
#     sum += i
# print('합계: ' + str(sum))

# 6. 홍길동 김길동 송길동 박길동 정길동을 계속 입력을 받고, x또는 X를 입력받으면 입력을 멈춤.
#    다음과 같이 출력. 첫번째 선수는 홍길동, 세번째 선수는 송길동
list = []
while True:
    name = input()
    list.append(name)
    if (name == 'x') or (name == 'X'):
        break

print('첫번째 선수는 ' + list[0] + ', 세번째 선수는 ' + list[2])
