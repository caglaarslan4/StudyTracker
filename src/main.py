from datetime import datetime
subjects=[]
study_sessions= []
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

def add_subject():
    count=int(input("How many subjects do you want to add: "))
    for i in range(count):
         subject=input("Enter subject name: ")
         subjects.append(subject)
         print(f"{subject} added succesfully.")

def list_subjects():
    if not subjects:
        print("No subject added yet. Please you should add your subjects.")
        return
    
    print("\n======== SUBJECTS ========")
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")

def add_study_session():
    if not subjects:
        print("No subjects added yet.")
        return

    print("ADD STUDY SESSİON".center(29,"="))
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")

    session=int(input("Chose a subject: "))
    while  session<1 or session>len(subjects):
        print("Invalid subject selection.")
        session=int(input("Chose a subject: "))
    
    selected_subject= subjects[session - 1]
    print(f"selected subject: {selected_subject}")

    duration=int(input("How many minutes did you study? "))
    while duration<=0:
        print("Invalid minutes selected.")
        duration=int(input("How many minutes did you study? "))
    print(f"You studied {duration} minutes for {selected_subject}.")

    current_time=datetime.now()
    study_session ={
        "subject":selected_subject,
        "duration":duration,
        "date":current_time.strftime("%d/%m/%Y"),
        "time":current_time.strftime("%H:%M")
    }
    study_sessions.append(study_session)
    print("study session added succesfully.")

def view_study_session():
    
    if not study_sessions:
        print("No study session yet.")
        return

    print("STUDY SESSİONS".center(30,"="))
    for sessions in study_sessions:
        print(f"Subject: {sessions['subject']}")
        print(f"Duration: {sessions['duration']}")
        print(f"Date: {sessions['date']}")
        print(f"Time: {sessions['time']}")
        print("-"*30)


    

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
        print("a")

    elif choice== "6":
        print("GOODBYE!")
        break 

    else:
        print("Invalid option!")