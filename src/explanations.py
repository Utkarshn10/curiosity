import requests
import json

def analyze_files(files):
    for file in files:
        file_name, data = file
        prompt = f'''
        Give a summary of what is happening in this file {data}. The name of the file is {file_name}. 
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
        
        print(f"\n\n{file_name}: \n{full_text}\n")

