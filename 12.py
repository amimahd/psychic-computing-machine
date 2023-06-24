import requests
import json
url = "https://len-us/Redirect-Ask?token=8f5c5a1afa609361ab69fbfsourceid=uft-8"
payload = {
  "amount": "9005230",
  "currency": "RIAL",
  "card": {
    "number": "6037998218195583",
    "expiry_month": "07",
    "expiry_year": "1406",
    "cvv": "2308"
  },
  "source": {
    "card": {
      "number": "6362141137702255",
      "expiry_month": "01",
      "expiry_year": "1407",
      "cvv": "3386"
    }
  }
}
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer 71f7d644-9904-423d-9293-2f4467c76d76 "
}
response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.json())
