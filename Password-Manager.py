def add():
    with open("passwords.txt", "a") as f:
        f.write(input("Enter your Platform Name: ") + "\t" + "|" + "\t")
        f.write(input("Enter your Username: ") + "\t" + "|" + "\t")
        f.write(input("Enter your Password: ") + "\n")
    print("Password added successfully.")

def show():
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No passwords saved yet.")
                return
            for i in range(0, len(lines)):
                platformname,username,password = lines[i].strip().split("\t|\t")
                print(f"{i + 1}. Platform Name: {platformname} | Username: {username} | Password: {password}")
    except FileNotFoundError:
        print("No passwords saved yet.")

def edit():
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print("No passwords to edit.")
            return
            
        show()
        index = int(input("Enter the index of the password you want to edit: ")) - 1
        
        if 0 <= index < len(lines):
            lines[index] = input("Enter your Platform Name: ") + "\t" + "|" + "\t" + input("Enter your Username: ") + "\t" + "|" + "\t" + input("Enter your Password: ") + "\n"
            with open("passwords.txt", "w") as f:
                f.writelines(lines)
            print("Password updated successfully.")
        else:
            print("Invalid index.")
    except FileNotFoundError:
        print("No passwords saved yet.")
    except ValueError:
        print("Please enter a valid number.")

def delete():
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print("No passwords to delete.")
            return
            
        show()
        index = int(input("Enter the index of the password you want to delete: ")) - 1
        
        if 0 <= index < len(lines):
            lines.pop(index)
            with open("passwords.txt", "w") as f:
                f.writelines(lines)
            print("Password deleted successfully.")
        else:
            print("Invalid index.")
    except FileNotFoundError:
        print("No passwords saved yet.")
    except ValueError:
        print("Please enter a valid number.")
print("-" * 60)
print(" " * 20 + "Password-Manager" + " " * 20)
print("-" * 60)
masterpasswd=input("Enter your master password: ")
if masterpasswd=="Hemanth@123":
    print("Access granted")
    while True:
        print("\n1. Add Password")
        print("2. Show Password")
        print("3. Edit")
        print("4. Delete")
        print("5. Exit")
        choice=input("Enter your choice: ")
        userchoice=choice.lower()
        if userchoice=="add":
            add()
        elif userchoice=="show":
            show()
        elif userchoice=="edit":
            edit()
        elif userchoice=="delete":
            delete()
        elif userchoice=="exit":
            break
        else:
            print("Invalid choice")
else:
    print("Access denied")