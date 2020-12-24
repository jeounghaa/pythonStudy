food = ['감자', '고구마', '양파']

life = [] # life = list()

print(food)
print(food[0])
print(len(food))
print(food[-1])
print(food[:2])

food[0] = 'cake'
print(food)

food.append('coffee')
print(food)

food.insert(0, 'rice')
print(food)

food.remove('rice') # 값을 가지고 삭제
print(food)

del food[0] # 인덱스를 가지고 삭제
print(food)

life.append('여행')
print(life)

print(food + life)

total = food + life
print(total)
total2 = food * 2
print(total2)

print(life)

life.append('집')
life.append('차')
life.append('돈')
life.append('')

myList = "Tis is a book That is a pencil".split()
print(type(myList))
print(myList)

foods = "apple banana melon coffee".split()



