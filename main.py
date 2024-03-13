import openai
import os
import datetime

def initialize_openai_client():
    # Initializes the OpenAI client using the API key from environment variables.
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OpenAI API key must be set in the 'OPENAI_API_KEY' environment variable.")
    return openai.OpenAI(api_key=api_key)

def get_unique_hello_world(client):
    # Generates a unique 'Hello, World!' message based on the current system time.
    current_time = datetime.datetime.now()
    friendly_time = current_time.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
    date_str = current_time.strftime("%Y-%m-%d")
    
    prompt = f"Given it's currently {friendly_time} on {date_str}, craft a unique 'Hello, World!' message, creatively incorporating the time and date."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )

    try:
        last_message = response.choices[0].message.content.strip()
    except IndexError:
        last_message = "Failed to generate a unique message."

    return last_message

def main():
    client = initialize_openai_client()
    unique_hello_world = get_unique_hello_world(client)
    print(unique_hello_world)

if __name__ == "__main__":
    main()
