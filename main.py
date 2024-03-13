import openai
from dotenv import load_dotenv
import os
import random
import datetime

load_dotenv()  # Load environment variables from .env file.

def initialize_openai_client():
    # Initializes the OpenAI client using the API key from environment variables.
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OpenAI API key must be set in the 'OPENAI_API_KEY' environment variable.")
    return openai.OpenAI(api_key=api_key)

def calculate_message_travel_time(planet_name):
    # Average distances from Earth to planets in kilometers
    planet_distances = {
        "Mercury": 91691000,
        "Venus": 41400000,
        "Earth": 0,
        "Mars": 78340000,
        "Jupiter": 628730000,
        "Saturn": 1275000000,
        "Uranus": 2723950000,
        "Neptune": 4351400000,
    }
    speed_of_light_km_per_s = 299792
    distance = planet_distances.get(planet_name, 0)
    time_seconds = distance / speed_of_light_km_per_s
    time_hours = time_seconds / 3600
    print(time_hours)
    return time_hours

def get_unique_hello_world(client):
    # Asks for a seed number and uses it to seed the random number generator.
    seed = input("Enter a seed number: ")
    random.seed(seed)
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_name = random.choice(planets)
    
    current_time = datetime.datetime.now()
    friendly_time = current_time.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
    date_str = current_time.strftime("%Y-%m-%d")
    travel_time_hours = calculate_message_travel_time(planet_name)
    
    prompt = f"Given it is currently {friendly_time} on {date_str}, craft a unique 'Hello, World!' message, creatively saying hello to the planet {planet_name}. Assume the message travels at the speed of light; it would take approximately {travel_time_hours:.2f} hours to reach {planet_name}. comment on this delay in your message if its relevant"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Please respond with a short and sweet message for the planet."},
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