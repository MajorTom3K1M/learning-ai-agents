import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <your_prompt>")
        sys.exit(1)
    else:
        user_prompt = " ".join(sys.argv[1:])
        print("User prompt:", user_prompt)
    
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=user_prompt,
        )
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print("Response:", response.text)



if __name__ == "__main__":
    main()
