# creating class with name student
class Student :
# constructor which initializes variable
   def __init__(self, name, roll_no):
    self.name = name
    self.roll_no = roll_no

# method to read the details from user
   def read(self):
    name = input("\nStudent name : ")
    roll_no = int(input("Roll no. : "))
    ob = Student(name,roll_no)
    list.append(ob)

# method to display details
   def display(self, ob) :
    print("\nStudent Name : ",ob.name)
    print("Roll no : ",ob.roll_no)

# method to search the entry
   def search(self, roll):
    for i in range(list.__len__()):
        if(list[i].roll_no == roll):
            print("\nStudent found!!")
            obj.display(list[i])
            return i
    print("\nStudent not found!!")

# method to delete an entry
   def delete(self, roll):
    n = obj.search(roll)
    del list[n]

# method to update an entry
   def update(self, roll, num, name_):
    n = obj.search(roll)
    roll_n = num
    list[n].roll_no = roll_n
    list[n].name = name_


# menu to execute the program
list = []
obj = Student(" ",0)
choice = 0
while(choice!=6):
    print("\n*******MENU*******\n")
    print("1.Read the details of student\n2.Display details\n3.Search details of student\n4.Delete details of student\n5.Update details\n6.Exit")
    choice = int(input("\nEnter your choice : "))

    if(choice==1):
        obj.read()
    elif(choice==2):
        print("\nDetails of students : ")
        for i in range(list.__len__()):
            obj.display(list[i])
    elif(choice==3):
        s = int(input("Enter the roll number to be searched : "))
        obj.search(s)
    elif(choice==4):
        d = int(input("Enter the roll number to be deleted : "))
        obj.delete(d)
        print("\nList after deletion : \n")
        for i in range(list.__len__()):
            obj.display(list[i])
    elif(choice==5):
        r = int(input("Enter the roll number to be replaced : "))
        u = int(input("Enter the updated roll number : "))
        n = input("Enter new name : ")
        obj.update(r,u,n)
        print("\nList after updation : \n")
        for i in range(list.__len__()):
            obj.display(list[i])
    elif(choice==6):
        print("THANK YOU!!")
# if choice is any other number than 1 to 6
    else:
        print("Invalid option!!")

"""
Output :
*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 1
Student name : esha
Roll no. : 1

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 1
Student name : maithili
Roll no. : 2

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 1
Student name : nitya
Roll no. : 3

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 1
Student name : barkha
Roll no. : 4

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 1
Student name : vinita
Roll no. : 5

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 2
Details of students :
Student Name : esha
Roll no : 1
Student Name : maithili
Roll no : 2
Student Name : nitya
Roll no : 3
Student Name : barkha
Roll no : 4
Student Name : vinita
Roll no : 5

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 3
Enter the roll number to be searched : 5
Student found!!
Student Name : vinita
Roll no : 5

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 4
Enter the roll number to be deleted : 1
Student found!!
Student Name : esha
Roll no : 1
List after deletion :
Student Name : maithili
Roll no : 2
Student Name : nitya
Roll no : 3
Student Name : barkha
Roll no : 4
Student Name : vinita
Roll no : 5

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 5
Enter the roll number to be replaced : 2
Enter the updated roll number : 6
Enter new name : clara
Student found!!
Student Name : maithili
Roll no : 2
List after updation :
Student Name : clara
Roll no : 6
Student Name : nitya
Roll no : 3
Student Name : barkha
Roll no : 4
Student Name : vinita
Roll no : 5

*******MENU*******
1.Read the details of student
2.Display details
3.Search details of student
4.Delete details of student
5.Update details
6.Exit
Enter your choice : 6
THANK YOU!!
Process finished with exit code 0
"""
