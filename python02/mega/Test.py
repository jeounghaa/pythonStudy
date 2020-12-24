# 주민번호를 입력받아서 여자/남자 판별

# ssd = input('주민번호를 입력해주세요 >> ')
# if (ssd[7] == '2') or (ssd[7] == '4'):
#     print('여자')
# elif (ssd[7] == '1') or (ssd[7] == '3'):
#     print('남자')
# else:
#     print('다시 입력해주세요.')


# 현재 시각을 입력받아서 11시 전이면 굿모닝, 15시 전이면 굿애프터눈, 20시 전이면 굿이브닝
# 그것도 아니면 굿나잇

# time = input('현재 시간을 입력해주세요(hh:mm) >> ')
# t = int(time[:2])
# if t < 11:
#     print('굿모닝')
# elif 11 <= t < 15:
#     print('굿애프터눈')
# elif 15 <= t < 20:
#     print('굿이브닝')
# else:
#     print('굿나잇')
    
    
# 인기투표 시스템 아이유, 공유, 유재석 중 계속 투표를 하다가
# 멈추고 싶을 때 멈추게
# 멈출 때, 각 투표수 프린트
vote = [0, 0, 0]
while True:
    s = input('아이유(1), 공유(2), 유재석(3) 중 투표(멈추기: 0) >> ')
    if s == '1':
        vote[0] += 1
    elif s == '2':
        vote[1] += 1
    elif s == '3':
        vote[2] += 1
    elif s == '0':
        print('아이유: ' + str(vote[0]) + ', 공유: ' + str(vote[1]) + ', 유재석: ' + str(vote[2]))
        break
    else:
        print('다시 선택해주세요')
