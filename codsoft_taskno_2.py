print("\n**Calculator**")

while True:

    a=int(input("\nEnter the 1st number : "))
    b=int(input("Enter the 2nd number : "))

    print("\nOperations :")
    print("1.Addition")
    print("2.subtraction")
    print("3.Multiplication")
    print("4.Division")

    choice=int(input("\nEnter your choice : "))

    if choice==1:
        sum=a+b
        print("\nAddition is : ",sum)

    elif choice == 2:
        sub=a-b
        print("\nSubtraction is : ",sub)

    elif choice == 3:
        mul=a*b 
        print("\nMultiplication is : ",mul)

    elif choice ==4:
        if b!=0:
            div=a/b 
            print("\nDivision is : ",div)
        else:
            print("\n Cannot divide by 0")    

    
    else:
       print("Enter valid number.!!")   

    c=input("\nDo next calculation ? (y/n)")    

    if c=="no" or c=="n":
        print("Exit!!!")
        break
    

    

