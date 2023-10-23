import requests
import json

if __name__ == "__main__":
    response = requests.post('http://172.21.2.6:5000/getDronePos')
    jsonResult = json.loads(response.content.decode('utf-8'))
    print(jsonResult)