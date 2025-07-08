# X Post Generator

A Python tool to generate concise, engaging, and professional posts for X (formerly Twitter) using an AI model.

## Features

- Generates posts up to 280 characters, tailored to a user-provided topic.
- Avoids hashtags, emojis, and special characters.
- Maintains a professional tone without personal opinions or biases.
- Interacts with a local AI model via HTTP API for post generation.

## How It Works

1. **User Input:**  
    The user is prompted to enter a topic for the X post.

2. **Prompt Construction:**  
    The tool builds a detailed prompt for the AI, specifying requirements for tone, length, and style.

3. **API Request:**  
    Sends the prompt and conversation history to a local AI model (`qwen3:4b`) via a POST request to `http://localhost:11434/api/chat`.

4. **Streaming Response:**  
    Receives the generated post in a streaming fashion, handling errors and assembling the final content.

5. **Output:**  
    Displays the generated post to the user.

## Usage

1. Ensure you have a local AI model running and accessible at `http://localhost:11434/api/chat`.
2. Install dependencies:
    ```bash
    pip install requests
    ```
3. Run the script:
    ```bash
    python <script_name>.py
    ```
4. Follow the prompts to enter your topic and receive your generated post.

## Example

```
Welcome to the X post generator!
This tool will help you create engaging posts for X (formerly Twitter).
--------------------------------------------------
Please provide a topic for the post.
**************************************************
Enter the topic for the X post: Artificial Intelligence in Healthcare
--------------------------------------------------
Here is your generated X post:
[Generated post appears here]
--------------------------------------------------
```

## Requirements

- Python 3.x
- `requests` library
- Local AI model API (compatible with the script)
- ollama running on your system

## Installing Ollama

If you don't have Ollama installed, you can find installation instructions on the [Ollama website](https://ollama.com/download). Follow the guide for your operating system to set up the required local AI model API.


## License

MIT License
