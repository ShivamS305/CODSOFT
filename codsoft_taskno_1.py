tasks=[]

print("\n** To Do List Application **")
while True:
    print("\n1.Add task")
    print("2.Update task")
    print("3.Complete Task")
    print("4.Display Task")
    print("5.Exit")

    c=int(input("\nEnter your choice : "))

    if c==1:
        a=input("Enter your task : ")
        tasks.append(a)
        print(f"\nYour {a} task is added.!!!")

    elif c==2:
        a=int(input("Enter the index number : "))-1
        b=input("Enter the task : ")
        if a<len(tasks):
            tasks[a]=b
            print(f"\nYour {b} task is updated.!!!")
        else:
            print("Enter valid index number") 

    elif c==3:
        a=int(input("Enter index number : "))-1
        if a <=len(tasks): 
            tasks[a]+=" - completed.!!"
            print("Your task is completed.!!!")
        else:
            print("\ntask not found")   

    elif c==4:
        for idx,el in enumerate(tasks):
            print(idx+1,".",el) 

    elif c==5:
        print("\nProgram End.!!!")
        break

    else:
        print("Enter valid number")



        