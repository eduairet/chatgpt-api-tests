"""Simple ChatGPT API Python program"""

import os
from dotenv import load_dotenv


# Environment Variables
load_dotenv()
apiKey = os.getenv("CHATGPT_API_KEY")


def main() -> str:
    """This function takes a prompt, passes it to ChatGPT and returns a string with the response"""
    prompt: str = input("Write your prompt here: ")
    print(prompt)


if __name__ == "__main__":
    main()
