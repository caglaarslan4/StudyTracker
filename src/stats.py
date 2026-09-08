from models import subjects, study_sessions

def show_statistics():
    print("\n======== STATİSTİCS ========")
    print(f"Total number of subjects: {len(subjects)}")

    total_minutes=0
    for session in study_sessions:
        total_minutes+= session["duration"]

    print(f"Total study time: {total_minutes} minutes")

    if study_sessions:
        average = total_minutes / len(study_sessions)
        print(f"Average study time: {average:.1f} minutes")
    else:
        print("Average study time: 0 minutes")

    print("=============================")