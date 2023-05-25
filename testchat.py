import openai
import gradio

openai.api_key = "INSERT_KEY_HERE"

message_history = []

def chat(prompt, role="user"):
    message_history.append({"role": role, "content": prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message_history
    )
    
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content

demo = gradio.Interface(fn = chat, inputs = "text", outputs = "text", title = "Basic Chatbot")

demo.launch()