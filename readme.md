
# hello_world_gpt

Inspired by a talk I saw last year at GDC, I wanted to create a very simple boilerplate "Hello World" program that prompts the OpenAI ChatGPT model with the current time to return a "Hello, World!" message. This project was developed with the assistance of GitHub Copilot, and I release it under the MIT License, allowing for wide usage, modification, and distribution.

Read about the included [Examples](https://github.com/bradenleague/hello_world_gpt/wiki)

Read more of my AI musings  [AI Curious](https://brae.page/personal/2024/02/26/AI-Curious.html)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system.

## Setup

To set up the project environment, follow these steps:

1. **Create a virtual environment:**

    ```
    python -m venv env
    ```

2. **Activate the virtual environment:**

    - On Windows:
        ```
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source env/bin/activate
        ```

3. **Install the required packages:**

    ```
    pip install openai python-dotenv
    ```

## Configuring Environment Variables

To securely manage your application's configuration (e.g., API keys), you will use environment variables. This project uses the `python-dotenv` package to load environment variables from a `.env` file.

1. **Create a `.env` file in the root directory of your project.**

2. **Add your environment variables to the `.env` file.**

    For example, to set the OpenAI API key, add the following line to your `.env` file:

    ```
    OPENAI_API_KEY=your_api_key_here
    ```

    Replace `your_api_key_here` with your actual OpenAI API key.

## Running the Application

Once the virtual environment is activated and you're in the project directory, execute the script by running:

```
python main.py
```

Enjoy!
