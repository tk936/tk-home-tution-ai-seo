import os
import requests
import json

def publish_to_gmb():
    # Credentials from GitHub Secrets
    api_key = os.getenv("GEMINI_API_KEY")
    access_token = os.getenv("GMB_ACCESS_TOKEN") # OAuth Token
    account_id = os.getenv("GMB_ACCOUNT_ID")   # Aapka Google Account ID
    location_id = os.getenv("GMB_LOCATION_ID") # Aapki Listing ID

    # 1. Content Generation (As per your 100 rules)
    areas = ["Mansarovar", "Vaishali Nagar", "Jagatpura", "Malviya Nagar"]
    landmarks = ["WTP", "GT Mall", "Albert Hall"]
    
    prompt = f"Write a professional GMB post for 'TK Home Tuition Jaipur'. Use landmark {random.choice(landmarks)} and area {random.choice(areas)}. Mention 'Verified Tutors' and 'Free Demo Class'. CTA: Call 9XXXX-XXXXX."
    
    # Gemini AI Call
    ai_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    ai_resp = requests.post(ai_url, json={"contents": [{"parts": [{"text": prompt}]}]})
    post_text = ai_resp.json()['candidates'][0]['content']['parts'][0]['text']

    # 2. Posting to Google (Connecting to your link)
    gmb_url = f"https://mybusiness.googleapis.com/v4/accounts/{account_id}/locations/{location_id}/localPosts"
    
    post_data = {
        "languageCode": "en-IN",
        "summary": post_text,
        "callToAction": {
            "actionType": "CALL",
            "url": "tel:9XXXX-XXXXX"
        }
    }

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(gmb_url, json=post_data, headers=headers)
    
    if response.status_code == 200:
        print("✅ Success: Post Live on Google Maps!")
    else:
        print(f"❌ Error: {response.text}")

if __name__ == "__main__":
    publish_to_gmb()
