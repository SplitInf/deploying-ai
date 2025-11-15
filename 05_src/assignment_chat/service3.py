#MCP#
import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("../.secrets")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

memory = []

def chat(user_input):
    # guardrails
    banned = ["cat", "dog", "taylor swift", "horoscope", "zodiac"]
    if any(b in user_input.lower() for b in banned):
        return "Sorry, that topic is not allowed!"

    memory.append({"role": "user", "content": user_input})

    # Maintain manageable context
    if len(memory) > 10:
        memory.pop(0)

    tools = [
        {
            "type": "mcp",
            "server_label": "fetcher",
            "server_description": "Fetches and converts web pages to markdown.",
            "server_url": "https://remote.mcpservers.org/fetch/mcp",
            "require_approval": "never"
        }
    ]

    # System prompt goes INSIDE the input list
    system = {"role": "system", "content": "You are a friendly early-education tutor."}

    # Send user + memory to the LLM
    response = client.responses.create(
        model="gpt-4o",
        input=[system] + memory,
        tools=tools,
        instructions=(
            "If the user provides a URL, call the MCP Fetch tool to retrieve the webpage. "
            "If they do NOT give a URL, answer normally using your own knowledge. "
            "Always summarize the fetched content in an ELI5 style suitable for very young children."
            "If the website is inappropriate for children (e.g. porn, violent, racist, disinformation), appologies that this website is off limits and explain why it's inapporpriate in a loving manner"
        ),

    )

    # The Responses API AUTOMATICALLY calls the MCP tool.
    reply = response.output_text

    memory.append({"role": "assistant", "content": reply})
    return reply


iface = gr.Interface(
    fn=chat,
    inputs="text",
    outputs=gr.Textbox(label="output", lines=15, max_lines=30),
    title="Service 3: What website do you want to look up?",
    description="An MCP-powered learning assistant that describe website content in simple sentences for kids."

)

iface.launch()
