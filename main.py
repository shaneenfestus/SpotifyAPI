import base64
from urllib.parse import urlencode
import requests
import datetime

client_id = 'c1b3e2df71a643e39ff0b14d76ba47bc'  # client id from spotify
client_secret = '757bee4c859d4929876d9f2b171e4fa0'  # client secret from spotify

# do a lookup for a token
# this token is for future requests

client_creds = f"{client_id}:{client_secret}"  # why f string?
type(client_creds)

client_cred_b64 = base64.b64encode(client_creds.encode())  # bytes encoded
type(client_cred_b64)

token_url = "https://accounts.spotify.com/api/token"
method = "POST"
token_data = {
    "grant_type": "client_credentials"

}
token_headers = {
    "Authorization": f"Basic {client_cred_b64.decode()}"  # base 64 encoded
}

r = requests.post(token_url, data=token_data, headers=token_headers)
print(r.json())
token_response_data = r.json()

now = datetime.datetime.now()
access_token = token_response_data['access_token']
expires_in = token_response_data['expires_in']
expires = now + datetime.timedelta(seconds=expires_in)
print(access_token)

headers = {
    "Authorization": f"Bearer {access_token}"
}
endpoint = "https://api.spotify.com/v1/search"
data = urlencode({"q": "Time", "type": "track"})
lookup_url = f"{endpoint}?{data}"
r = requests.get(lookup_url, headers=headers)
print(r.status_code)

data = urlencode({"q": "2 Weeks", "type": "track"})
lookup_url = f"{endpoint}?{data}"
r = requests.get(lookup_url, headers=headers)
r.json()

