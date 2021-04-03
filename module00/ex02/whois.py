from sys import argv
num = 0
num = int(argv[1])
if num==0:
    print("I'm zero")
if num>0 :
    if (num % 2) == 0:
        print("I'm Even")
    else:
        print("I'm Odd")

