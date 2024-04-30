import requests
class ClientInfer:
    def __init__(self,server_address) -> None:
        self.url = server_address

    def infer(self,text):
        data = {
            "text": text  # Replace this with the actual text you want to send
        }
        api_link = '/process-text/'
        response = requests.post(self.url+api_link, json=data) 
        try:
            if response.status_code == 200:
                print("Response from server:", response.json())
                return response.json()
            else:
                print("Error:", response.status_code) 
        except:
            return 10
    
    
if __name__ == '__main__':
    client = ClientInfer(server_address='http://0.0.0.0:9096')
    while True:

        text = input(">> User: ")
        if '/bye' in text:
            break
        
        y_hat = client.infer(text=text)
        print(f'<< AI: {y_hat}')
    
        