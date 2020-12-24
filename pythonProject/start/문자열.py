company = 'mega company' # "를 써도 됨
company2 = 'mega company' \
            '신촌에 있음' \
            '여기는 7층'
print(company)
print(company2)

company3 = '''mega company
                나는 여러줄 치는거야.
                또 나야.
                또또 나'''
print(company3)

result = True
print('결과는 ' + str(result)) # 파이썬에서는 결합시키는 경우에는 타입이 동일해야함

n1 = int(input('숫자1입력>> '))
n2 = int(input('숫자2입력>> '))
print(n1+n2)