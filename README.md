# ChatGPT API Tests

## Configuration

-   Set your api key in an `.env` file at root level and write your API key

    ```
    CHATGPT_API_KEY=YourApiKeyGoesHere
    ```

-   Create your environment and activate it

    ```BASH
    python3 -m venv .venv # You need python installed and configured
    . .venv/bin/activate
    ```

-   Install the dependencies

    ```BASH
    # Make sure your using .venv pip with which pip
    pip install -r requirements.txt
    ```

-   Now you can run the scripts in the scripts folder

    ```BASH
    # Make sure your using .venv pip with which python
    python scripts/script001.py
    ```
