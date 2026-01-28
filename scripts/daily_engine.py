import os
import requests
import datetime
import random

# TK Home Tuition Data
AREAS = ["Mansarovar", "Vaishali Nagar", "Jagatpura", "Malviya Nagar", "C-Scheme", "Raja Park", "Bani Park", "Sanganer"]
LANDMARKS = ["WTP Mall", "Gaurav Tower", "Albert Hall", "Akshardham Temple", "Statue Circle", "Jawahar Circle"]
SUBJECTS = ["Maths", "Science", "Commerce", "Class 10 Board", "Class 12 Board", "English"]

def run_tk_ai():
    api_key = os.getenv("GEMINI_API_KEY")
    area = random.choice(AREAS)
    landmark = random.choice(LANDMARKS)
    subject = random.choice(SUBJECTS)
    
    # Prompt as per your 100 features condition
    prompt = (f"Act as a Local SEO Expert for 'TK Home Tuition Jaipur'. "
              f"Create a GMB post for {area} near {landmark} targeting {subject}. "
              f"Include: 'Verified Tutors', 'Free Demo Class', 'Safe for Girls', 'Result Oriented'. "
              f"Add a daily logical quiz question. "
              f"CTA: Call 9XXXX-XXXXX for Home Tuition in Jaipur. Use Hinglish.")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=payload)
        post_text = response.json()['candidates'][0]['content']['parts'][0]['text']
        
        # Dashboard Update Logic
        log_content = f"\n### 📅 Date: {datetime.date.today()}\n**📍 Area:** {area} | **🏛️ Landmark:** {landmark}\n\n**📝 Post Content:**\n{post_text}\n\n---\n"
        
        with open("DASHBOARD.md", "a", encoding="utf-8") as f:
            f.write(log_content)
        print("Success: Dashboard Updated")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_tk_ai()
