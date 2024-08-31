'''Create a program that manages a list of student
names, allowing the user to add, remove, and
display the list.'''

#defing function for student Management
def student_det(choice,student_list):  
   
    #for Adding Name in list
    if choice==1:
        name=input("Enter Name:")
        if name in student_list:
            print("Already Available")
        else:
            student_list.append(name)
            print("Student Added",student_list)
   
    #for Deleting Name from the list
    elif choice==2:
        name=input("Enter Name:")
        if name in student_list:
            student_list.remove(name)
            print("Student Removed",student_list)
        else:
            print("Name not found")
   
    #for Displaying the list of student
    elif choice==3:
        print(student_list)
    else:
        print("Invalid choice")

#Pre Define List
student_list=["satyam","mohan"] 

#taking the choice 
choice=int(input("what you want \n"
                 "01. For Add Name \n"
                 "02. For Delete Name \n"
                 "03. FOr Display Name \n"))  
student_det(choice,student_list)