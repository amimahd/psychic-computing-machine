import requests
import json
import random

api_url = 'https://https://tikweb.net:2083/execute/some_api_endpoint'
username = 'karenrah'
password = '7vE120Lrup'
payload = {
    'param1': 'value1',
    'param2': 'value2'
}

api_key = '71f7d644-9904-423d-9293-2f4467c76d76'
merchant_id = '14011004-7659941170|P4652500'
amount = 500000000
source_number = '4541655255'
destination_number = '0303806377009'
callback_url = 'https://www.bmi.ir/callback'
order_id = random.randint(1000, 9999)

data = {
    'api-key': api_key,
    'amount': amount,
    'order_id': order_id,
    'source_number': source_number,
    'destination_number': destination_number,
    'merchant_id': merchant_id,
    'callback_url': callback_url
}

headers = {
    'Authorization': f'cpanel {username}:{password}',
    'Content-Type': 'application/json'
}


# Make a POST request to the Sadad API endpoint
response = requests.post(api_url, json=payload, headers=headers)
if response.status_code == 200:
    print('POST request succeeded')
    print('Response:', response.json())
else:
    print('POST request failed')
    print('Error:', response.text)

