#Kacey Wheeler
#AP Computer Science: 2A
#2/19/19
#Unit 8 Labs
#Leap Year

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")



