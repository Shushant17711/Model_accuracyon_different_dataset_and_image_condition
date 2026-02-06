# Model_accuracyon_different_dataset_and_image_condition

## Google Drive Setup for Research Project

This repository includes a script to automatically create a structured folder hierarchy in Google Drive for organizing your research project.

### Folder Structure

The script creates the following folder structure in your Google Drive:

```
Research_Project/
├── data/
├── models/
└── results/
```

- **data/**: Store datasets and raw data files
- **models/**: Store trained model files and checkpoints
- **results/**: Store experimental results, metrics, and visualizations

### Prerequisites

1. Python 3.7 or higher
2. Google Cloud account with Google Drive API enabled
3. OAuth 2.0 credentials from Google Cloud Console

### Setup Instructions

#### 1. Enable Google Drive API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Drive API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Drive API"
   - Click "Enable"

#### 2. Create OAuth 2.0 Credentials

1. In Google Cloud Console, go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. Choose "Desktop app" as the application type
4. Download the credentials JSON file
5. Rename it to `credentials.json` and place it in the project root directory
   - See `credentials.json.example` for the expected format

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Usage

Run the script to create the folder structure in your Google Drive:

```bash
python create_gdrive_folders.py
```

The script will:
1. Open a browser window for Google authentication (first time only)
2. Request permission to access your Google Drive
3. Create the Research_Project folder with subfolders
4. Save authentication token for future use

### First Run

On the first run, you'll be prompted to:
1. Log in to your Google account
2. Grant permission to the application to manage Google Drive files

After successful authentication, a `token.pickle` file will be created to store your credentials for future runs.

### Files Generated

- `token.json`: Stores authentication tokens (do not commit to version control)
- `credentials.json`: OAuth 2.0 credentials (do not commit to version control)

### Important Notes

**API Scope**: This script uses the `drive.file` scope, which only grants access to files and folders created by the application. This is a security best practice that limits access to only the folders created by this script. The script cannot access or modify other files in your Google Drive.

**Duplicate Prevention**: The script checks for existing folders before creating new ones, so it's safe to run multiple times.

### Security Notes

⚠️ **Important**: Never commit `credentials.json` or `token.json` to version control. These files contain sensitive authentication data.

Add them to `.gitignore`:
```
credentials.json
token.json
```

### Troubleshooting

**Error: "credentials.json not found"**
- Make sure you've downloaded and renamed your OAuth credentials file

**Authentication issues**
- Delete `token.json` and run the script again to re-authenticate

**Permission errors**
- Ensure the Google Drive API is enabled in your Google Cloud project
- Verify your OAuth consent screen is properly configured

### License

This project is open source and available under the MIT License.