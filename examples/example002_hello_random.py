import openai
from dotenv import load_dotenv
import os
import datetime
import platform
import random

load_dotenv()  # Load environment variables from .env file.

# ANSI escape codes for some colors
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
}

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

def get_random_color_code():
    # Picks a random color and returns its ANSI code
    color_name = random.choice(list(colors.keys()))
    color_code = colors[color_name]
    return color_code, color_name

def get_unique_hello_world(client):
    # Generates a unique 'Hello, World!' message based on the current system time and OS version.
    current_time = datetime.datetime.now()
    friendly_time = current_time.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
    date_str = current_time.strftime("%Y-%m-%d")
    system_info = get_system_info()
    os_version = system_info['os_version']
    machine = system_info['processor']
    
    prompt = f"Given it is currently {friendly_time} on {date_str} and the OS version is {os_version} on {machine}, craft a unique 'Hello, World!' message, creatively incorporating the time, date, and OS version."

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
    color_code = get_random_color_code()
    # This assumes that color_code is a tuple like this: ('\033[94m', 'blue'). If the structure of color_code is different, you'll need to adjust the indexing accordingly.
    print(color_code[0] + unique_hello_world + ".\033[0m")

if __name__ == "__main__":
    main()