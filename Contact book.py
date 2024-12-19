#Creating the greeting message to display.

print("Welcome to the Contact Application")
print("Here you can store, search, delete and update the contacts")
print("-------------------------------------------------")

#making empty list to store the names and numbers
names = []
numbers = []

#Here we are using the loop to running untill user quit
while True:
    print("\nContact Book ") #Display menu options
    print("-------------------------------------------")
    print("1. Add a name and number ")
    print("2. Search for a name")
    print("3. Delete a name and number")
    print("4. Update a name and number")
    print("5. Close the Contact book")
    
       #get input from the user
    choice = input("Choose the option(1-5): ")
    
      #for adding the contact
    if choice == '1':
        name = input("Enter the contact name: ")
        if name in names:
            print(f"Contact '{name} = {number}' already exists.")
        else:
            number = input("Enter Contact phone number: ")
            names.append(name)
            numbers.append(number)
            print(f"Contact'{name}' added successfully.")
            
      #Search for the contact
    elif choice == '2':
        name = input("Enter the name to search: ")
        if name in names:
            index = names.index(name)
            print(f"Contact found - '{name} = {number}'") 
        else:
            print("Contact not found.")
            
          #Delete a Contact
    elif choice == '3':
          print("Enter the name to delete: ")
          if name in names:
              index = names.index(name)
              names.pop(index)
              numbers.pop(index)  
              print(f"Contact '{name}' deleted successfully.")
          else:
              print("Contact not found!")
             
         #updating the existing contact    
              
    elif choice == '4':
        name = input("Enter the name to update: ")
        if name in names:
            index = names.index(name)
            new_number = input(f"Enter the new number for '{name}': ")
            numbers[index] = new_number
            print(f"Contact '{name}' updated successfully.")
        else:
            print("Contact not found!")
            break    
    #Exit the program
    
    elif choice == '5':
        print("Exiting the program. Goodbye!") 
        break
    
    #Handle the invalid or False inf0
    else:
      print("Invalid. Please enter the correct option(1-5)")       
        
                                      