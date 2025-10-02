import random

#1
def ouncesCalculator(grams : int):
    ounces = 28.3495231 * grams
    return ounces

#2
def Fahrenheit(F : int):
    C = int((5 / 9) * (F - 32))
    return  C

#3
def solve(numheads, numlegs):
    rabbits = 0.5 * numlegs - numheads    
    chickens = 2 * numheads - 0.5 * numlegs

#4
def isPrime(n : int):
    if(n == 1): return False
    if(n == 2): return True
    if(n % 2 == 0): return False

    p = int(n ** 0.5) + 1

    for i in range(3, p, 2):
        if n % i == 0: return False
    return True
def filterPrime(a):
    for i in a:
        if isPrime(i):
            print(i, end= ' ')

#5
def nextPermutation(mi):
    if len(mi) <= 1:
        print(*mi)
        return False
    firstIndex = 0
    lastIndex = len(mi)
    i = lastIndex - 1
    while True:
        ii = i
        i -= 1
        if mi[i] < mi[ii]:
            j = lastIndex - 1
            while not mi[i] < mi[j]:
                j -= 1
            mi[i], mi[j] = mi[j], mi[i]
            mi[ii:lastIndex] = mi[ii:lastIndex][::-1]
            return True
        if i == firstIndex:
            mi[firstIndex:lastIndex] = mi[firstIndex:lastIndex][::-1]
            return False
    return False 

#6
def reversedSentencen(s):
    answ = ""
    for i in s:
        answ = i + " " + answ
    return answ

#7
def checkThree(n):
    b = len(n)
    for i in range(b):
        if(b - 1 == i): return False
        if(n[i] == 3 and n[i + 1] == 3): return True

#8
def agentOOZ(n):
    cnt = 0
    for i in n:
        if(cnt <= 2 and i == 0):
            cnt += 1
        elif(cnt == 2 and i == 7):
            cnt += 1
            break
    if(cnt == 3):
        return True
    return False

#9
def volumeOfSphere(r):
    volume = (4 / 3) * 3.14 * (r ** 3)
    print(volume)

#10
def unique(n):
    answ = []
    for i in n:
        if(not i in answ):
            answ.append(i)
    return answ

#11
def isPalindrome(s):
    i = 0
    j = len(s) - 1

    while(i < j):
        if(s[i] == s[j]):
            i += 1
            j -= 1
        else:
            return False
    return True

#12
def histogram(a):
    for i in a:
        for j in range(i):
            print('*', end = '')
        print()

#13
def guessNumber():
    print("Hello! What is your name?")
    name = input()
    print()

    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    n   = int(input())
    print()

    a   = random.randrange(1, 20, 1)
    cnt = 0

    while(n != a):
        cnt += 1

        if(n < a):
            print("Your guess is too low.")
            print("Take a guess.")
        elif(n > a):
            print("Your guess is big")
            print("Take a guess")

        n = int(input())
        print()
    
    print("Good job, " + name + "! You guessed my number in " + str(cnt) + " guesses!")