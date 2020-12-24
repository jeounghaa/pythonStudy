food = ['감자', '고구마', '양파']

# for, for-each
for x in food:
    print(x, end=' ')

print()

for i in range(0, 3): # 0~2
    print(food[i])

print()

for i in [0, 1, 2]:
    print(food[i])

# subject = []
# # 입력을 5번 받아서 리스트에 넣으세요
# for i in range(0, 5):
#     s = input('입력 >> ')
#     subject.append(s)
#
# for x in subject:
#     print(x, end="\t")
# print()
# for i in range(0, len(subject)):
#     print(subject[i])

jumsu = []
sum = 0
for i in range(0, 5):
    s = input('점수 입력 >> ')
    jumsu.append(s)
    sum += int(s)

print('평균: ' + str(sum/len(jumsu)))


