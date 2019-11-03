#Kacey Wheeler
#AP Computer Science: 2A
#2/19/19
#Unit 8 Labs
#Leap Year

#Get user input for year
year = int(input("Enter a year: "))

#If year is divisible by 4
if year % 4 == 0:
    #If year is divisible by 100
    if year % 100 == 0:
        #If year is divisible by 400
        if year % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")



