# AI Deployment assignment 2 – Services 1, 2, and 3

This project implements a 3-service AI application using OpenAI models, ChromaDB, function calling, and the Model Context Protocol (MCP). The system is built with Gradio as the user interface and demonstrates web scraping, semantic search, persistent vector storage, and tool-integrated reasoning.

## Service 1 — News Summarizer for Children

Purpose:
Takes a news article (via thenewsapi.com API), calls GPT-4o to summarize it in a child-friendly way

Key features:

Fetches news and summarizes stories in a digestable format.

Summaries are rewritten in ELI5 style.

Includes a scoring system (1–5) based on educational + fun value.

## Service 2 — Semantic Search with ChromaDB

Purpose:
Creates a searchable embedding database of scraped full-text articles.

Steps:

Scrapes article URLs from Service 1 using newspaper3k.

Embeds text using text-embedding-3-small.

Inserts vectors + metadata into a persistent ChromaDB instance.

Key features:

Provides semantic search: users type a natural-language question and system returns the most relevant articles.

## Service 3 — MCP-Powered Webpage Fetch & ELI5 Summarizer

Purpose:
Uses an MCP tool (“Fetch” server) to automatically retrieve a webpage and summarize it for children.

Key features:

User enters a URL and the Responses API automatically calls the fetch tool retrieves the webpage HTML and GPT-4o summarizes the content in kindergarten-friendly language.

If user enters a non URL, the system will try its best to answer.

Addition:

- Guardrails block questions about cats, dogs, horoscopes / zodiac, and Taylor Swift

- The app keeps a sliding window of the last 10 messages:


## Running the Project
python service1.ipynb
python service2.ipynb
python service3.py

For service3.py, Gradio interfaces will appear in your browser.