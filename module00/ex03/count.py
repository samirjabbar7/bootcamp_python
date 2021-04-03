from sys import argv

def text_analyzer (char):
    upper, lower, punctuation , space = 0, 0, 0, 0

    for i in range(len(char)):
        if(char[i].isupper()):
            upper += 1
        elif(char[i].islower()):
            lower += 1
        elif(char[i]==" "):
            space += 1
        elif(char[i] in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?")):
            punctuation += 1
    print('sum of upper-case characters:', upper)
    print('sum of lower-case characters:', lower)
    print('sum of punctuation characters:', punctuation)
    print('sum of space characters:', space)
  

char = argv[1]

text_analyzer(char)
