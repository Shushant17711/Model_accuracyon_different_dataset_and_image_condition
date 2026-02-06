#!/usr/bin/env python3
"""
Script to create Research_Project folder structure in Google Drive.

This script creates the following folder structure:
- Research_Project/
  - data/
  - models/
  - results/

Requirements:
- Google Drive API credentials (credentials.json)
- google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-python-client packages
"""

import os.path
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']


def authenticate_google_drive():
    """
    Authenticate with Google Drive API.
    
    Returns:
        Resource object for interacting with Google Drive API
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    service = build('drive', 'v3', credentials=creds)
    return service


def create_folder(service, folder_name, parent_id=None):
    """
    Create a folder in Google Drive.
    
    Args:
        service: Google Drive API service instance
        folder_name: Name of the folder to create
        parent_id: ID of the parent folder (None for root)
    
    Returns:
        ID of the created folder
    """
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    
    if parent_id:
        file_metadata['parents'] = [parent_id]
    
    try:
        folder = service.files().create(
            body=file_metadata,
            fields='id, name'
        ).execute()
        
        print(f'Created folder: {folder.get("name")} (ID: {folder.get("id")})')
        return folder.get('id')
    
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None


def create_research_project_structure():
    """
    Create the Research_Project folder structure in Google Drive.
    """
    print("Authenticating with Google Drive...")
    service = authenticate_google_drive()
    
    print("\nCreating Research_Project folder structure...")
    
    # Create main Research_Project folder
    research_project_id = create_folder(service, 'Research_Project')
    
    if research_project_id:
        # Create subfolders
        subfolders = ['data', 'models', 'results']
        
        for subfolder in subfolders:
            create_folder(service, subfolder, research_project_id)
        
        print("\n✓ Successfully created Research_Project folder structure!")
        print("\nFolder structure created:")
        print("Research_Project/")
        print("├── data/")
        print("├── models/")
        print("└── results/")
    else:
        print("\n✗ Failed to create Research_Project folder")


if __name__ == '__main__':
    create_research_project_structure()
