>>> print("---------猜数字---------")
import random
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)
answer = a * 1000 + b * 100 + c * 10 + d
counts = 100
while counts > 0:
    temp = input("猜一猜我心里的四位数字吧哈哈哈：")
    guess = int(temp)
    e = guess // 1000
    f = ( guess - e * 1000) // 100
    g = ( guess - e * 1000 - f * 100) // 10
    h = ( guess - e * 1000 - f * 100 - g * 10)
    if guess == answer:
        print("你猜对啦")
        print("不过猜对了也没有奖励,嘻嘻嘻~~~")
        print("游戏结束啦")
        counts = counts - 1
        print("次数:",end="");print(100 - counts)
        break
    else:
        print("次数：",end="");print(101- counts)
        if a == e:
            print("第一位对喽")
        if b == f:
            print("第二位对喽")
        if c == g:
            print("第三位对喽")
        if d == h:
            print("第四位对喽")    
        if guess > answer:
            print("不过大了呢快快快继续继续")
            print("继续猜吧")
        else:
            print("不过小了呢")
