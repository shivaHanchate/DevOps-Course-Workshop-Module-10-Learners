import requests

url = "https://login.microsoftonline.com/832ff4a4-3177-4d9b-a91f-932943c2a009/oauth2/v2.0/token"

payload='client_id=01f6ae12-d07a-4942-83d4-20721830e28c&scope=api%3A%2F%2Fd5a32b8f-9043-4181-ae6f-66141a56b1c2%2F.default&client_secret=~gK1VHY58KE30YGed_5mzG1N0Aa.JZm~Ln&grant_type=client_credentials'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'x-ms-gateway-slice=estsfd; stsservicecookie=estsfd; fpc=AmASKEDEy3ZEoe6AuaQGG5tDpXI1AwAAAEJcONgOAAAA'
}

response = requests.request("POST", url, headers=headers, data=payload).json()
Authorize_token = response["access_token"]


get_url = "https://localhost:5001/WeatherForecast"

get_payload={}
get_headers = {
  'Authorization': 'Bearer ' + Authorize_token
}

get_response = requests.request("GET", get_url, headers=get_headers, data=get_payload).json()

print(get_response)