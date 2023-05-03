import openai
import os

def get_response_from_chatgpt(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )

    return result["choices"][0]["message"]["content"]

def get_transcript():
    data = ''

    with open('transcript.txt', 'r') as file:
        data = file.read().replace('\n', ' ')

    return data

def construct_prompt(transcript):
    return "Can you summarize the following transcript?\n{}".format(transcript)

def one_line_summary(transcript):
    return "Can you summarize the following in one sentence?\n{}".format(transcript)

def make_shorter(transcript):
    return "Can you make this shorter?\n{}".format(transcript)