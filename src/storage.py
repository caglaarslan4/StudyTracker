from models import subjects,study_sessions
import json

def save_data():
    with open("data.json","w") as file:
        data ={
            "subjects":subjects,
            "study_sessions":study_sessions
        }

        json.dump(data,file)

def load_data():
    try:
        with open("data.json","r") as file:
          
          data= json.load(file)
          subjects.clear()
          subjects.extend(data["subjects"])

          study_sessions.clear()
          study_sessions.extend(data["study_sessions"])
    except FileNotFoundError:
        print("No saved data found. Starting with empty data.")
    
