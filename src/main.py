from study_manager import (
    add_subject,
    list_subjects,
    add_study_session,
    view_study_session,
    delete_subject,
    delete_study_session
    

)
from stats import show_statistics
from storage import load_data
from storage import save_data

def show_menu():

    print("***********************")
    print("     STUDY TRACKER     ")
    print("***********************")
    print("1. Add subject")
    print("2. List subjects")
    print("3. Add study session")
    print("4. View session")
    print("5. Show statistics")
    print("6. Delete subject")
    print("7. Delete study session")
    print("8. Exit")

load_data() 

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
        delete_subject()

    elif choice== "7":
        delete_study_session()

    elif choice== "8": 
        print("GOODBYE!")  
        save_data()
        break

    else:
        print("Invalid option!")