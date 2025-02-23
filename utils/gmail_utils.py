# gmail_utils.py
import base64
import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists("config/token.json"):
        creds = Credentials.from_authorized_user_file("config/token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('config/client_secret_162468226544-e1ebqgtngc46jbvt3il2374fhshnkrlh.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open("config/token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def fetch_emails(service, label_ids=["INBOX"], max_results=10):
    # Fetch emails from Gmail inbox
    results = service.users().messages().list(userId="me", labelIds=label_ids, maxResults=max_results).execute()
    messages = results.get("messages", [])
    email_contents = []

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        email_data = {}
        email_data["id"] = msg["id"]
        email_data["snippet"] = msg_data["snippet"]
        
        # Get headers
        headers = msg_data["payload"]["headers"]
        for header in headers:
            if header["name"] == "From":
                email_data["from"] = header["value"]
            if header["name"] == "Subject":
                email_data["subject"] = header["value"]
        
        email_contents.append(email_data)

    return email_contents
