life = '인생은 짧다. 길게 살자..!'

print(life[0])
print(life[-1]) # -인덱스 존재: 끝에서 시작!
print(life[-2])

# 반복문(자바에서는 -1을 입력하지만, 파이썬에서는 조심)

life2 = life * 10
print(life2)

print('i like {0} money{1}'.format(1000, '원'))

print(life2.find('i'))
print(life2.find('짧'))

life3 = ", ".join('abcd')
print(life3)

life4 = "            all space          "
print(life4.rstrip())
print(life4.lstrip())
print(life4.strip())
print(life4.replace('all', 'some'))
print(life4.split()) # 공백을 기준으로 단어 분리

life5 = '재미있게 삽시다!! 신나게.....~'
print(life5)
print(life5[0:4])
print(life5[:4])
print(life5[1:])

if life5 == life4:
    print('동일해요')
else:
    print('동일하지 않아요')
