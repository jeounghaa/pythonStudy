# print('welcome!')

# 명령어 == 함수 == function == method
# 기능을 사용함

# 기능을 정의한다. 함수를 정의한다.
# def 함수명():
#   들여쓰기한 다음 실행하는 것 쭉 구현

class Dog:
    name = '홍길동'
    def __init__(self):
        print('내가 생성자 함수!')


    def bark(self):
        print('강아지가 짖다.')

    def __str__(self):
        return self.name


def print2():
    print('나는 프린트를 2번 하겠음')
    print('나는 프린트를 2번 하겠음')


if __name__ == '__main__':
    print2()

    dog1 = Dog()
    dog1.bark()
    print(dog1)

# print2(); # 호출한다.(call)
# print2();