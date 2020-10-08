num = 1
limit = 20

while (num < limit):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz",end=",")
        num = num +1
        continue
    elif num % 3 == 0:
        print("Fizz",end=",")
        num = num +1
        continue
    elif num % 5 == 0:
        print("Buzz",end=",")
        num = num +1
        continue
    
    print(num,end=",")
    num = num +1

