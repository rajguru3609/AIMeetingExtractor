from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_meeting(transcript):
    prompt = f"""
You are an expert meeting assistant.

Here is a meeting transcript:

{transcript}

Please provide:

1. A concise summary of the meeting
2. Key points discussed
3. Action items, including who is responsible if mentioned
4. Decisions made
5. A professional follow-up email
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
