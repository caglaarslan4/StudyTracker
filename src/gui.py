import tkinter as tk
from datetime import datetime

from models import subjects, study_sessions
from storage import save_data


def add_subject_gui():
    subject = subject_entry.get().strip()

    if not subject:
        return

    subjects.append(subject)

    subject_entry.delete(0, tk.END)

    subject_listbox.insert(tk.END, subject)

    save_data()


def add_study_session_gui():
    selected_index = subject_listbox.curselection()

    if not selected_index:
        return

    selected_subject = subject_listbox.get(selected_index[0])

    duration_text = duration_entry.get().strip()

    if not duration_text:
        return

    if not duration_text.isdigit():
        return

    duration = int(duration_text)

    if duration <= 0:
        return

    current_time = datetime.now()

    study_session = {
        "subject": selected_subject,
        "duration": duration,
        "date": current_time.strftime("%d/%m/%Y"),
        "time": current_time.strftime("%H:%M")
    }

    study_sessions.append(study_session)

    duration_entry.delete(0, tk.END)

    session_listbox.insert(
        tk.END,
        f"{selected_subject} - {duration} minutes - "
        f"{study_session['date']} {study_session['time']}"
    )

    save_data()


root = tk.Tk()

root.title("Study Tracker")
root.geometry("600x600")
root.resizable(False, False)


# ---------------- TITLE ----------------

title_label = tk.Label(
    root,
    text="STUDY TRACKER",
    font=("Arial", 20)
)
title_label.pack(pady=15)


# ---------------- SUBJECT ----------------

subject_label = tk.Label(
    root,
    text="Add Subject",
    font=("Arial", 14)
)
subject_label.pack()


subject_entry = tk.Entry(
    root,
    width=30
)
subject_entry.pack(pady=5)


add_subject_button = tk.Button(
    root,
    text="Add Subject",
    command=add_subject_gui
)
add_subject_button.pack(pady=5)


subject_listbox = tk.Listbox(
    root,
    width=40,
    height=6
)
subject_listbox.pack(pady=10)


# ---------------- STUDY SESSION ----------------

session_label = tk.Label(
    root,
    text="Add Study Session",
    font=("Arial", 14)
)
session_label.pack(pady=5)


duration_label = tk.Label(
    root,
    text="Study duration (minutes):"
)
duration_label.pack()


duration_entry = tk.Entry(
    root,
    width=20
)
duration_entry.pack(pady=5)


add_session_button = tk.Button(
    root,
    text="Add Study Session",
    command=add_study_session_gui
)
add_session_button.pack(pady=5)


# ---------------- SESSION LIST ----------------

sessions_title = tk.Label(
    root,
    text="Study Sessions",
    font=("Arial", 14)
)
sessions_title.pack(pady=10)


session_listbox = tk.Listbox(
    root,
    width=70,
    height=8
)
session_listbox.pack()


root.mainloop()