import requests
import base64
import io
import json
import argparse

url = "http://localhost:8080/completion"
headers = {"Content-Type": "application/json"}

# Create the parser and add argument
parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True, help='Path to the image file')
args = parser.parse_args()

# Open the image file in binary mode and convert to base64
with open(args.path, 'rb') as file:
    encoded_string = base64.b64encode(file.read()).decode('utf-8')

image_data = [{"data": encoded_string, "id": 12}]

data = {"prompt": "USER:[img-12]Describe the image.\nASSISTANT:", "n_predict": 128, "image_data": image_data, "stream": True}

response = requests.post(url, headers=headers, json=data, stream=True)
print("Sent request to the server...")
print()
for chunk in response.iter_content(chunk_size=128):
    content = chunk.decode().strip().split('\n\n')[0]
    try:
        content_split = content.split('data: ')
        if len(content_split) > 1:
            content_json = json.loads(content_split[1])
            print(content_json["content"], end='', flush=True)
    except json.JSONDecodeError:
        break
