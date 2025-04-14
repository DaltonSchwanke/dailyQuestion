import json
import random
import datetime

def get_question():
    with open("questions.json", "r") as f:
        questions = json.load(f)

    today_tag = datetime.datetime.now().strftime("%A").lower()

    # Filter to today's questions that have not been used
    eligible = [q for q in questions if today_tag in q["tags"] and not q.get("used", False)]

    # If all have been used, optionally reset
    if not eligible:
        print("✅ All questions used — resetting...")
        for q in questions:
            q["used"] = False
        eligible = [q for q in questions if today_tag in q["tags"]]
    
    # Randomly select a question
    selected = random.choice(eligible)
    selected["used"] = True

    # Write updated list back to the file
    with open("questions.json", "w") as f:
        json.dump(questions, f, indent=2)

    return selected["question"]
