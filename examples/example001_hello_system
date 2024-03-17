import openai
from dotenv import load_dotenv
import os
import datetime
import platform

load_dotenv()  # Load environment variables from .env file.

def initialize_openai_client():
    # Initializes the OpenAI client using the API key from environment variables.
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OpenAI API key must be set in the 'OPENAI_API_KEY' environment variable.")
    return openai.OpenAI(api_key=api_key)

def get_system_info():
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }
    return system_info

def get_unique_hello_world(client):
    # Generates a unique 'Hello, World!' message based on the current system time and OS version.
    current_time = datetime.datetime.now()
    friendly_time = current_time.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
    date_str = current_time.strftime("%Y-%m-%d")
    system_info = get_system_info()
    os_version = system_info['os_version']
    
    prompt = f"Given it is currently {friendly_time} on {date_str} and the OS version is {os_version}, craft a unique 'Hello, World!' message, creatively incorporating the time, date, and OS version."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content.strip()

def main():
    client = initialize_openai_client()
    unique_hello_world = get_unique_hello_world(client)
    print(unique_hello_world)

if __name__ == "__main__":
    main()