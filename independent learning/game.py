>>> print("---------Guess Number---------")
import random
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)
answer = a * 1000 + b * 100 + c * 10 + d
counts = 100
while counts > 0:
    temp = input("Guess the four digits I have in mind :")
    guess = int(temp)
    e = guess // 1000
    f = ( guess - e * 1000) // 100
    g = ( guess - e * 1000 - f * 100) // 10
    h = ( guess - e * 1000 - f * 100 - g * 10)
    if guess == answer:
        print("You got it.")
        print("But there's no reward for guessing correctly~")
        print("Game over.")
        counts = counts - 1
        print("number of times:",end="");print(100 - counts)
        break
    else:
        print("number of times：",end="");print(101- counts)
        if a == e:
            print("The first one's right.")
        if b == f:
            print("The second one's right")
        if c == g:
            print("The third one's right")
        if d == h:
            print("The fourth one's right")    
        if guess > answer:
            print("But it's bigger. Come on, come on, come on. Keep going.")
            print("Continue")
        else:
            print("But it's smaller")
