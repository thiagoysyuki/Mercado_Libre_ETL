import requests
import json
import os
import webbrowser
import secrets
from dotenv import load_dotenv
from urllib.parse import  urlencode
import time

load_dotenv()

class ML_OAuth:
    def __init__(self):
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.redirect_uri = os.getenv('REDIRECT_URI')
        self.auth_url = "https://auth.mercadolivre.com.br/authorization"
        self.token_url = "https://api.mercadolibre.com/oauth/token"
        self.token = None
        self.refresh_token = None

    def get_authorization_code(self):
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state": secrets.token_urlsafe(16)
        }
        url = f"{self.auth_url}?{urlencode(params)}"
        webbrowser.open(url)
        print("Please authorize the application and provide the authorization code from the redirect URL.")

    def get_access_token(self, authorization_code):

        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        }
        
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "code": authorization_code
        }
        response = requests.post(self.token_url, data=data, headers=headers)

        token_data = response.json()
        self.token = token_data['access_token']
        self.refresh_token = token_data['refresh_token']
        print("Access Token:", self.token)
        print("Refresh Token:", self.refresh_token)

    def refresh_access_token(self):
        payload = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token
        }

        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(self.token_url, data=payload, headers=headers)
        token_data = response.json()
        self.token = token_data['access_token']
        self.refresh_token = token_data['refresh_token']
        print("New Access Token:", self.token)
        print("New Refresh Token:", self.refresh_token)
    
    def start_auth_process(self):
        self.get_authorization_code()
        autorization_code = input("Enter the authorization code from the redirect URL: ")
        self.get_access_token(autorization_code)
        loop_counter = 0
        while True:
           print("Waiting to refresh access token...")
           loop_counter += 1
           print(f"Refresh cycle: {loop_counter}")
           json_access = {'access_token': self.token}
           with open('access_token.json', 'w') as f:
               json.dump(json_access, f)
           time.sleep(21600)
           self.refresh_access_token()


if __name__ == "__main__":
    ml_oauth_instance = ML_OAuth()
    ml_oauth_instance.start_auth_process()