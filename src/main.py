subjects=[]
def show_menu():
    print("***********************")
    print("     STUDY TRACKER     ")
    print("***********************")
    print("1. Add subject")
    print("2. List subjects")
    print("3. Add study session")
    print("4. Show statistics")
    print("5. Exit")

def add_subject():
    subject=input("Enter subject name: ")
    subjects.append(subject)
    print(f"{subject} added succesfully.")

while True:
    show_menu()

    choice= input("Choose an option: ")

    if choice == "1":
        add_subject()

    elif choice == "2":
        print("List subeject selected")

    elif choice == "3":
        print("Add study session selected")

    elif choice == "4":
        print("Show statistics selected")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")