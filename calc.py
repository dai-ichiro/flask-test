import requests

url = 'http://localhost:5000/double'
data = {'number': 10}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(f"結果: {result['result']}")
else:
    print(f"エラー: {response.status_code}, {response.text}")