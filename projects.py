import random
print("Welcome to my applications")
print("This is a Mathematics quiz.")
print("Type '000' if you want to stop")
x = random.randint(1, 10)
y = random.randint(1, 10)
c = x * y
while True:
    print(x , "X" , y , "=")
    answer = int(input())
    if answer != c:
       if answer == 000:
           print("Thanks for playing!")
           break
       else:
            print("Wrong answer! The answer is:")
            print(c)
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            c = x * y
    else:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        c = x * y
        print("Correct answer!")
