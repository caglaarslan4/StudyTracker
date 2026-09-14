from datetime import datetime
from models import subjects, study_sessions
from utils import get_integer
from storage import save_data

def add_subject():
    count=get_integer("How many subjects do you want to add: ")
    for i in range(count):
         subject=input("Enter subject name: ")
         subjects.append(subject)
         save_data()
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

    session=get_integer("Chose a subject: ")
    while  session<1 or session>len(subjects):
        print("Invalid subject selection.")
        session=get_integer("Chose a subject: ")
    
    selected_subject= subjects[session - 1]
    print(f"selected subject: {selected_subject}")

    duration=get_integer("How many minutes did you study? ")
    while duration<=0:
        print("Invalid minutes selected.")
        duration=get_integer("How many minutes did you study? ")
    print(f"You studied {duration} minutes for {selected_subject}.")

    current_time=datetime.now()
    study_session ={
        "subject":selected_subject,
        "duration":duration,
        "date":current_time.strftime("%d/%m/%Y"),
        "time":current_time.strftime("%H:%M")
    }
    study_sessions.append(study_session)
    save_data()
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

def delete_subject():

    if not subjects:
        print("No subject available")
        return

    list_subjects()
    chose_subject=get_integer("Which subject do you want to delete:")
    if chose_subject<1 or chose_subject>len(subjects):
        print("Invalid subject selection.")
        return
    subjects.pop(chose_subject - 1)
    save_data()
    print("Subject deleted successfully")

def delete_study_session():
    if not study_sessions:
        print("No study session available.")
        return
    for i,session in enumerate(study_sessions, start=1):
        print(f"{i}. {session['subject']} - {session['duration']} minutes - {session['date']} {session['time']}")

    chose_session= get_integer("Which study session do you want to delete: ")
    if chose_session<1 or chose_session>len(study_sessions):
        print("Invalid study session selection.")
        return
    study_sessions.pop(chose_session - 1)
    save_data()
    print("Study session deleted successfully.")
    



