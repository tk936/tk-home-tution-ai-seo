import os
import requests
import datetime

def run_seo_engine():
    api_key = os.getenv('GEMINI_API_KEY')
    # Humne aapka number aur business details yahan fix kar di hain
    my_number = "9672616854"
    areas = ["Mansarovar", "Vaishali Nagar", "Jagatpura", "Malviya Nagar"]
    area = areas[datetime.datetime.now().day % len(areas)]
    
    prompt = f"Write a professional Hinglish GMB post for TK Home Tuition Jaipur in {area}. Mention Free Demo and Call {my_number}."
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    try:
        response = requests.post(url, json=payload)
        ai_text = response.json()['candidates'][0]['content']['parts'][0]['text']
        
        # Dashboard update karne ke liye text file mein likhna
        with open("DASHBOARD.md", "a") as f:
            f.write(f"\n## Update: {datetime.datetime.now()}\nArea: {area}\nPost: {ai_text}\n---\n")
        print("Success: Dashboard Updated")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_seo_engine()
