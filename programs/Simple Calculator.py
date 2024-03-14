def cal():
    print("\tSimple Calculator\t")
    NUM1 = int(input("Enter First Number: "))
    NUM2 = int(input("Enter Second Number:"))
    print("Select options:")
    usr = int(input("1)+\n2)-\n3)*\n4)/\n5)%\n"))
    if usr == 1:
        print(f"The Addition of two numbers is {NUM1+NUM2}")
    elif usr == 2:
        print(f"The Subtraction of two numbers is {NUM1-NUM2}")
    elif usr == 3:
        print(f"The Multiplication of two numbers is {NUM1*NUM2}")
    elif usr == 4:
        if NUM1 == 0:
            print("Divison not possible")
        else:
            print(f"The Divison of two numbers is {NUM1/NUM2}")
    elif usr == 5:
        print(f"The Modulus of two numbers is {NUM1%NUM2}")
    else :
        print("Invalid selection")
    
#calling function to execute
cal()
