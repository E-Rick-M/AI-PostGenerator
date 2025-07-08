import requests
import json
def generate_x_post(topic:str ,history:list)-> str:
    prompt=f"""You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter). Your task is to create a post that will capture the attention of users and encourage them to interact with it.
    Your task is to generate a post that is concise, engaging, and relevant to the topic at hand. The post should be no longer than 280 characters and tailored to the topic provided by the user.
    Avoid using hashtags, emojis, or any other special characters. The post should be written in a professional tone and should not include any personal opinions or biases.
    
    Here's the topic provided by the user for which you need to generate a post:
    
    <topic>
    {topic}
    </topic>
    """
   
    history.append({"role": "system", "content": prompt})
    response=requests.post("http://localhost:11434/api/chat",json={
        "model": "qwen3:4b",
        "messages": history,
        "stream":True,
    })

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    print("Response from the server:")
    content = ""
    for line in response.iter_lines():
        if line:
            try:
                data =json.loads(line)
                if data.get("done"):
                    break
                if "message" in data and data["message"].get("role") == "assistant":
                    chunk = data["message"].get("content", "")
                    content += chunk
                    print(chunk, end="", flush=True)
            except json.JSONDecodeError as e:
                print(f"Error processing line: {e}-Line: {line}")
                continue
    if not content:
        print("No content generated."+ "-" * 50)
        return None
    print("\nPost generation complete.")
    return content

def main():
    history = []
    print("Welcome to the X post generator!")
    print("This tool will help you create engaging posts for X (formerly Twitter).")
    print("-" * 50)
    print("Please provide a topic for the post.")
    print("**" * 50)
    input_topic = input("Enter the topic for the X post: ")
    history.append({"role": "user", "content": input_topic})
    post = generate_x_post(input_topic , history)

    print("-" * 50)
    print("Here is your generated X post:")
    print(post)
    print("-" * 50)

if __name__ == "__main__":
    main()
