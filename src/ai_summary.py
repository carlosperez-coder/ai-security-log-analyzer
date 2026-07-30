import os
from dotenv import load_dotenv
from openai import OpenAI


def generate_ai_summary(failed_logins, suspicious_ips):
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "AI summary skipped: OPENAI_API_KEY was not found in the .env file."
    
    if not suspicious_ips:
        return "No suspicious IPs were detected, so no AI incident summary was generated."
    
    client = OpenAI(api_key=api_key)

    prompt = f"""
You are a junior cybersecurity analyst. 

Analyze the following failed login activity and suspicious IP findings. 

Total failed login attempts: {len(failed_logins)}

Suspicious IP findings:
{suspicious_ips}

Write a clear incident summary with: 
1. What happened
2. Why this activity is suspicious
3. Which accounts were targeted
4. Recommend next investigation steps

Keep it beginner-friendly, professional, and concise. 
"""
    
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text

