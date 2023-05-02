import openai

def get_response_from_chatgpt(prompt):
    openai.api_key = "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"
    
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
    

    return f"Can you summarize the following transcript?\n{transcript}"