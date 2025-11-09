from pyautogui import write
from openai import OpenAI

question = input("What is your question?: ")

client = OpenAI(
    api_key=""
)

chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": question}
    ],
    max_tokens=250
)

response_text = chat_completion.choices[0].message.content
print("Go to where you want to write this in 10 seconds")
write(response_text)
