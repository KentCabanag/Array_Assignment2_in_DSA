#Write a python program that do the following:

#- display the initial content of the array
#- display a menu of options
#- allow user to select item in the menu (check if valid)
#- perform the selected option (you may prompt additional info to user when need)
#- display the resulting values of the array


#Note: 
#- The program has an array variable containing 10 random numbers
#- You may add other options and features
#- Your program should be uploaded to github before 1:30pm
#- Record a demo presenting your program
#- Send the demo directly to my messenger

#Example Output:

#Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
#Menu:
 #1 -> Add an element
 #2 -> Insert an element
 #3 -> Modify an element
 #4 -> Delete an element
 #5 -> Arrange in ascending order
 #6 -> Arrange in descending order
#What do you want to do? (1-6): 4
#Enter the index you want to delete: 3
#The element has been deleted
#This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]
Array = [6, 4, 2, 8, 10, 18, 14, 16, 12, 20]
print("Index Array :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]")
print(f"Array: {Array}")
print("Menu:")
print("Pick A number on this")
print("1 -> Add an element")
print("2 -> Insert an element")
print("3 -> Modify an element")
print("4 -> Delete an elementt")
print("5 -> Arrange in ascending order")
print("6 -> Arrange in descending order")
print()
Question = int(input("What do you want to do? "))
def num1():
    if Question == 1:
        Type_num = int(input("Type the Number that you want to add: "))
        Add = Array.append(Type_num)
        print("The Numbers has been Added")
        return Add

    elif Question == 2:
        Type_num2 = int(input("Type the Number that you want to insert: "))
        Type_num3 = int(input("Where do you want to insert? "))
        Add1 = Array.insert(Type_num3, Type_num2)
        print("The element has been Insert")
        return Add1
    
    elif Question == 3:
        Type_num4 = int(input("Type the index position do you want to Modify: "))
        Add2 = Array.pop(Type_num4)
        print("The element has been Modify")
        return Add2

    elif Question == 4:
        Type_5 = int(input("Type the Number that you want to Delete: "))
        Add3 = Array.remove(Type_5)
        return Add3

    elif Question == 5:
        Add4 = Array.sort()
        print("The element has been arrange to ascending order")
        return Add4

    elif Question == 6:
        Add5 = Array.reverse()
        print("The element has been arrange to descending order")
        return Add5


num1()
print()
print(f"This is the new array: Array : {Array}")
