"""Simple ChatGPT API Python program"""

import os
import openai
from dotenv import load_dotenv


# Environment configuration
load_dotenv()
apiKey = os.getenv("CHATGPT_API_KEY")
openai.api_key = apiKey

# Chat configuration
messages = [
    {"role": "system", "content": "Hi there! I am a chatbot."},  # System configuration
]


def main():
    """This function takes a prompt, passes it to ChatGPT and returns a string with the response"""
    while True:
        prompt = input("Write your prompt here: ")  # Asks user for a prompt
        if prompt:
            messages.append({"role": "user", "content": prompt})  # User configuration
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )  # Starts a chat
        reply = chat.choices[0].message.content  # Takes the first message in the chats
        print(f"ChatGPT: {reply}\n")  # And prints it
        messages.append(
            {"role": "assistant", "content": reply}
        )  # Adds the message to the messages list


if __name__ == "__main__":
    main()
