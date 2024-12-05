'''
Nick DeMaestri
12/5/2024
CS-391

Ollama Summarizer
'''

import requests
import json

file_name = "french_revolution.txt" # Change this to the name of the file you want to summarize, include the directory if the file is not in the same directory as this script.

file = open(file_name, "r")
file_text = file.read()

url = "http://localhost:11434/api/generate"

headers = { 
    "Content-Type": "application/json"
}

data = {
    "model": "llama2",
    "prompt": "Generate a 5 sentence summary of the following text, make sure the output is translated in French and is simple enough for even a 5th grader to understand: " + file_text,
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_text = response.text 
    data = json.loads(response_text)
    actual_response = data["response"]
    print(actual_response)
else:
    print("Error:", response.status_code, response.text)
