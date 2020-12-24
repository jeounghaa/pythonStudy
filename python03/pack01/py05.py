jumsu = {'철수': 100, '영희': 90}

print(jumsu['철수'])
jumsu['영희'] = 100
print(jumsu)

jumsu2 = dict(철수 = 100, 영희 = 90)
print(jumsu2)

del jumsu2['철수']
print(jumsu2)

jumsu2['순희'] = 80
print(jumsu2)

jumsu2['하양'] = 88
print(jumsu2)

for x in jumsu2:
    print(x)

for key in jumsu2:
    print(jumsu2[key])

# from tkinter import messagebox
# messagebox.showinfo("it's me!")
# result = messagebox.askquestion("ok??", "really??")
#
# print(result)
#
# if result == 'yes':
#     print('확인 완료')
# else:
#     print('다시 확인')

data = (1,2,3)
data2 = {1, 2, 3}
data3 = [1, 2, 3]
data4 = {'name': 'hong', 'age': 100}
print(type(data))
print(type(data2))
print(type(data3))
print(type(data4))


