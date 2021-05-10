import random

r = random.randint(1, 100)
while True:
    num = input('請猜猜看數字是多少: ') 
    num = int(num)
    if num == r :
        print('恭喜你,猜對了')
        break
    elif num > r :
        print('比答案大')
    elif num < r :
        print('比答案小')
