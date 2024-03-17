import openai
from dotenv import load_dotenv
import os
import random
import datetime

load_dotenv()  # Load environment variables from .env file.

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

def initialize_openai_client():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable must be set.")
    return openai.OpenAI(api_key=api_key)

def calculate_message_travel_time(planet_name):
    speed_of_light_km_per_s = 299792
    distance = planet_distances.get(planet_name, 0)
    time_seconds = distance / speed_of_light_km_per_s
    time_hours = time_seconds / 3600
    print(f"Message travel time to {planet_name}: {time_hours:.2f} hours")
    return time_hours

def generate_mech_name():
    prefixes = ['Aero', 'Nergal', 'Geo', 'Psycho', 'Black', 'Shadow', 'Neo', 'Solar', 'Lunar']
    infixes = ['buster', 'star', 'nova', 'giga', 'mega', 'beam', 'strike', 'lancer', 'ranger']
    suffixes = ['Rex', 'Zord', 'Tron', 'Gunner', 'Fighter', 'Knight', 'Warrior', 'Crusader', 'Pilot']
    prefix = random.choice(prefixes)
    infix = random.choice(infixes)
    suffix = " " + random.choice(suffixes)
    return f"{prefix}{infix}{suffix}"

def get_unique_hello_world(client):
    seed = input("Enter a seed number: ")
    random.seed(seed)
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_name = random.choice(planets)
    
    current_time = datetime.datetime.now()
    friendly_time = current_time.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
    date_str = current_time.strftime("%Y-%m-%d")
    travel_time_hours = calculate_message_travel_time(planet_name)
    
    mech_name = generate_mech_name()  # Generate a mech name to include in the message.
    
    prompt = f"Given it is currently {friendly_time} on {date_str}, and considering a mech named {mech_name} is sending a 'Hello, World!' message to planet {planet_name}, creatively craft this message. Assume the message travels at the speed of light, taking approximately {travel_time_hours:.2f} hours to reach {planet_name}. Comment on this delay if relevant."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Please respond to the mech with a succinct and sweet message."},
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