# 1(year)3153600 second
# 1(year)525600 minute
# 1(year)8760 hour
# 1(year)365 day
# 1(year)52.1 week
# 1(year)12 month
print("-----------------------------------------------------------------")
print("Hello")
myname = input("what is your name : ")
myAge = input("Enter your year of birth : ")
dataofnow = input("Enter what year it is : ")
myAge = int(myAge)
dataofnow = int(dataofnow)
myAge = dataofnow - myAge
while myAge < 0 :
    print("An error occurred Try again")
    myAge = input("Enter your year of birth : ")
    dataofnow = input("Enter what year it is : ")
    myAge = int(myAge)
    dataofnow = int(dataofnow)
    myAge = dataofnow - myAge    
print("---------")
print(F"Well,{myname} please see : ")
print("---------")
second = myAge * 31536000
minute = myAge * 525600
hour = myAge * 8760
day = myAge * 365
week = myAge * 52
month = myAge * 12
print(F"You have {myAge} years old")
print("~~~~~~~~~~~~~~~~~~")
print(F"month : {month}")
print("~~~~~~~~~~~~~~~~~~")
print(F"week : {week}")
print("~~~~~~~~~~~~~~~~~~")
print(F"day : {day}")
print("~~~~~~~~~~~~~~~~~~")
print(F"hour : {hour}")
print("~~~~~~~~~~~~~~~~~~")
print(F"minute : {minute}")
print("~~~~~~~~~~~~~~~~~~")
print(F"second : {second}")
print("~~~~~~~~~~~~~~~~~~")
print("Programmer : Houshmand")
print("*-*-*-*-*-*-*-*-*-*-*-*")
Exit = input("if you want exit write'exit'and if you whant try it again write'again' : ").lower()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
again = "again"
while Exit == again:                         # loop
    myname = input("what is your name : ")
    myAge = input("Enter your year of birth : ")
    dataofnow = input("Enter what year it is : ")
    myAge = int(myAge)
    dataofnow = int(dataofnow)
    myAge = dataofnow - myAge
    myAge = int(myAge)
    while myAge < 0 :
        print("An error occurred Try again")
        myAge = input("Enter your year of birth : ")
        dataofnow = input("Enter what year it is : ")
        myAge = int(myAge)
        dataofnow = int(dataofnow)
        myAge = dataofnow - myAge    
    print("---------")
    print(F"Well,{myname} please see : ")
    print("---------")
    myAge = int(myAge)
    second = myAge * 31536000
    minute = myAge * 52560
    hour = myAge * 8760
    day = myAge * 365
    week = myAge * 52
    month = myAge * 12
    print(F"You have {myAge} years old")
    print("~~~~~~~~~~~~~~~~~~")
    print(F"month : {month}")
    print("~~~~~~~~~~~~~~~~~~")
    print(F"week : {week}")
    print("~~~~~~~~~~~~~~~~~~")
    print(F"day : {day}")
    print("~~~~~~~~~~~~~~~~~~")
    print(F"hour : {hour}")
    print("~~~~~~~~~~~~~~~~~~")
    print(F"minute : {minute}")
    print("~~~~~~~~~~~~~~~~~~")
    print(F"second : {second}")
    print("~~~~~~~~~~~~~~~~~~")
    print("Programmer : Houshmand")
    print("*-*-*-*-*-*-*-*-*-*-*-*")
    Exit = input("if you want exit write'exit'and if you whant try it again write'again' : ").lower()
    if Exit == "exit" or Exit == "quit":
        break

# END
#Houshmand-2005_
