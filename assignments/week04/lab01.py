"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("mark",0,"Bangbo","Thailand")  # name, age, city, country
    hobbies = ["Game"]
    
    # Your code here
    while True:

        print("1 Display all info, 2 Add hobby, 3 Remove hobby, 4 Edit age, 5 exit")
        choice = input("Choose option:")
        
        if choice == "1":
                print("Name: ", person[0])
                print("Age: ", person[1])
                print("City : ", person[2])
                print("Country: ", person[3])
                print("Hobbies: ", hobbies)

        elif choice =="2":
                hobby = input("Insert new hobbies: ")
                hobbies.append(hobby)
            
        elif choice =="3":
                del hobbies[0]

        elif choice =="4":
                age = int(input("Insert new age: "))
                person_list = list(person)
                person_list[1] = age
                person = tuple(person_list)
            
        elif choice =="5":
            break

if __name__ == "__main__":
    personal_info_manager()
