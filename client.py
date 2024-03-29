import requests

# URL of the FastAPI server
url = "http://113.203.209.145:9096/process-text/"

# Data to be sent to the server
data = {
    "text": "Yes, I am 26 years old."  # Replace this with the actual text you want to send
}

# Sending a POST request to the FastAPI server
response = requests.post(url, json=data)

# Checking if the request was successful
if response.status_code == 200:
    print("Response from server:", response.json())
else:
    print("Error:", response.status_code)
