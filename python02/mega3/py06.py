class TV:
    company = 'mega'
    color = 'red'
    size = 50

    def __init__(self):
        print('tv가 만들어졌습니다.')


    def turn_on(self):
        print('tv를 켜다')


    def turn_off(self):
        print('tv를 끄다')


    def __str__(self):
        return 'company: ' + self.company + ', color: ' \
               + self.color + ', size: ' + str(self.size)

