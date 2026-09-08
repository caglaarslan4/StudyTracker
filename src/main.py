from study_manager import (
    add_subject,
    list_subjects,
    add_study_session,
    view_study_session

)
from stats import show_statistics

def show_menu():

    print("***********************")
    print("     STUDY TRACKER     ")
    print("***********************")
    print("1. Add subject")
    print("2. List subjects")
    print("3. Add study session")
    print("4. View session")
    print("5. Show statistics")
    print("6. Exit")

while True:
    show_menu()

    choice= input("Choose an option: ")

    if choice == "1":
        add_subject()

    elif choice == "2":
        list_subjects()

    elif choice == "3":
        add_study_session()
        
    elif choice == "4":
        view_study_session()

    elif choice == "5":
        show_statistics()

    elif choice== "6":
        print("GOODBYE!")
        break 

    else:
        print("Invalid option!")