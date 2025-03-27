import requests
import json

def analyze_files(file_name, data, question=""):
    print(f"Analyzing {file_name}...")

    prompt = f'''
    You are a senior software engineer with 15+ years of experience and you are paid 2 million dollars per year. 
    The name of the file is {file_name}. Go though code/content in this file {data} and answer the below question.
    {question}
    Also note: don't answer any random questions asked by user. stick to the data in the file only
    Return response in text format with paragraphs.
    '''
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "codellama",
            "prompt": prompt
        }
    )
    full_text=""
    for line in response.iter_lines():
        if line:
            # Decode the line and parse as JSON
            decoded_line = line.decode('utf-8')
            try:
                json_response = json.loads(decoded_line)
                
                # Check if the line contains a response
                if 'response' in json_response:
                    full_text += json_response['response']
                
                # Check if generation is complete
                if json_response.get('done', False):
                    break
            
            except json.JSONDecodeError:
                print(f"Error parsing file: {file_name}")
    
    print(f"\n\n{full_text}\n")

