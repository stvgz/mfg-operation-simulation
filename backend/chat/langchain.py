import openai
import os

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

def generate_text(prompt, max_tokens=100):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def translate_text(text, source_lang, target_lang):
    prompt = f"{source_lang}: {text}\n{target_lang}:"
    return generate_text(prompt)

def ask_code_question(question, max_tokens=100):
    prompt = f"Translate the following English text to Python code: {question}"
    return generate_text(prompt, max_tokens)

def langchain(question):
    code = ask_code_question(question)
    return code



if __name__ == "__main__":
    pass