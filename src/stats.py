from models import subjects, study_sessions

def show_statistics():
    print("\n======== STATİSTİCS ========")
    print(f"Total number of subjects: {len(subjects)}")

    total_minutes=total_study_time()

    print(f"Total study time: {total_minutes} minutes")

    if study_sessions:
        average = total_minutes / len(study_sessions)
        print(f"Average study time: {average:.1f} minutes")
    else:
        print("Average study time: 0 minutes")

    subject_times={}
    for session in study_sessions:
        subject= session["subject"]
    
        if subject not in subject_times:
            subject_times[subject]=0

        subject_times[subject]+=session["duration"]

    longest_subject=""
    longest_minutes=0
    for subject,minutes in subject_times.items():
        print(f"{subject}: {minutes} minutes")
        if minutes > longest_minutes:
            longest_minutes=minutes
            longest_subject=subject
    print(f"The most studied subject: {longest_subject} - {longest_minutes} minutes.")
    

    print("=============================")

def total_study_time():
    total=0
    for session in study_sessions:
        total+=session["duration"]
    return total

    