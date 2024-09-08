# Google Integration Portal

This project is a Django-based web portal that allows users to view and manage Google My Business reviews from a centralized platform. The portal leverages the Google My Business API to fetch and display reviews and allows users to reply to these reviews directly from the portal.

## Key Features

- **Google Authentication**: Secure access through Google OAuth 2.0.
- **View Google Reviews**: Fetch and display Google My Business reviews.
- **Reply to Reviews**: Respond to reviews directly from the portal.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: Google My Business API, OAuth 2.0

## Prerequisites

- **Python 3.6+**
- **Django 3.x+**
- **pip** (Python package installer)
- **Google Cloud Account** with access to the [Google Cloud Console](https://console.cloud.google.com/)

## Getting Started

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository

Clone this repository to your local machine.

```bash
git clone https://github.com/Dolly-Ardeshana/google-review-integratin-portal.git
cd google-review-integratin-portal
```

### 2. Create a Virtual Environment

Create and activate a virtual environment to manage dependencies.

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```
### 3. Install the Required Dependencies

Install the required packages using pip

```bash
pip install -r requirements.txt
```

### 4. Obtain Google OAuth 2.0 Credentials

To use Google Authentication and access the Google My Business API, you need to create OAuth 2.0 credentials. Follow the steps below to obtain your `CLIENT_ID` and `CLIENT_SECRET`.

#### Steps to Obtain `CLIENT_ID` and `CLIENT_SECRET`:

1. **Go to the [Google Cloud Console](https://console.cloud.google.com/).**

2. **Create a New Project**:
   - Click on the project dropdown at the top of the page and select **New Project**.
   - Enter a project name and select a billing account (if prompted).
   - Click **Create** to create a new project or select an existing project.

3. **Enable APIs**:
   - Navigate to **APIs & Services > Library** in the left sidebar.
   - Search for and enable the following APIs:
     - **Google My Business Account Management API**
     - **Google My Business Business Information API**

4. **Create OAuth 2.0 Credentials**:
   - Go to **APIs & Services > Credentials**.
   - Click on **Create Credentials** and select **OAuth 2.0 Client ID**.

5. **Configure the Consent Screen**:
   - If prompted, configure the OAuth consent screen:
     - Choose **External** for the User Type.
     - Enter the required information (app name, user support email, etc.).
     - Click **Save and Continue** to configure the scopes and other settings.

6. **Set the Application Type**:
   - Under the **Create OAuth client ID** section, set the **Application type** to **Web application**.
   - Enter a name for your OAuth client (e.g., "Google Integration Portal").

7. **Add Authorized Redirect URIs**:
   - In the **Authorized redirect URIs** section, click **Add URI**.
   - Add the following URI for local development:  
     `http://localhost:8000/oauth2callback/`

8. **Generate Credentials**:
   - Click **Create** to generate your `CLIENT_ID` and `CLIENT_SECRET`.
   - A popup will display your `CLIENT_ID` and `CLIENT_SECRET`. Copy these values or click **Download** to save the credentials file in JSON format.

9. **Save Your Credentials**:
   - Store the `CLIENT_ID` and `CLIENT_SECRET` in a secure place.
   - You will use these credentials in your application to authenticate users and access the Google My Business API.

> **Note**: Ensure that your `CLIENT_ID` and `CLIENT_SECRET` are properly configured in your environment variables as described in Step 5.

### 5. Set Up Environment Variables

Create a .env file in the root directory of your project to store the Google OAuth credentials and the Django secret key.

Create a .env file

```bash
touch .env
```
Add the following content to the .env file:

```bash
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
```
### 6. Go to Project folder

Run the following commands to go to project google_integration_portal.

```bash
cd google_integration_portal
```

### 7. Apply Migrations and Run the Server

Run the following commands to apply database migrations and start the development server.

Create a .env file

```bash
python manage.py migrate
python manage.py runserver
```
Open your web browser and navigate to http://localhost:8000/ to access the portal.

## Project Structure

The project is organized as follows:

- **`reviews/`**: Django app for managing Google My Business reviews.
- **`templates/`**: HTML templates for rendering the web pages.
- **`static/`**: Static files (CSS, JavaScript).
- **`requirements.txt`**: List of required Python packages.

## Usage

Follow these steps to use the portal:

1. **Login with Google**: 
   - Click the "Login with Google" button on the homepage to authenticate using your Google account.
   - Ensure you allow the required permissions for accessing Google My Business data.

2. **View Reviews**:
   - After logging in, you will see a list of reviews fetched from your Google My Business account.
   - The reviews will be displayed with details like the reviewer's name, rating, and comments.

3. **Reply to Reviews**:
   - Next to each review, you will find a form or input field to submit a reply.
   - Enter your response and click the "Reply" button to post your reply directly to the review.

## Troubleshooting

If you encounter any issues while running the application, refer to the following troubleshooting tips:

- **Quota Exceeded Errors**: 
  - If you receive an error like `HttpError 429`, it indicates that you have exceeded the quota for Google API requests.
  - To resolve this, consider optimizing your API usage or requesting a quota increase from the [Google Cloud Console](https://console.cloud.google.com/).

- **OAuth 2.0 Errors**: 
  - If you face issues with OAuth 2.0 authentication, ensure that your `CLIENT_ID` and `CLIENT_SECRET` are correctly set in your `.env` file.
  - Verify that the redirect URI (`http://localhost:8000/oauth2callback/` for local development) is correctly configured in the Google Cloud Console under your OAuth 2.0 Client ID settings.


## Additional Setup Information

1. **Install `python-dotenv`**: Make sure that `python-dotenv` is listed in `requirements.txt` if you are using environment variables.
2. **Update `requirements.txt`**: Include all necessary Python packages, such as:
   - `Django`
   - `google-auth`
   - `google-auth-oauthlib`
   - `google-auth-httplib2`
   - `google-api-python-client`
   - `python-dotenv`

By following this `README.md` file, you and other developers can easily set up and run the project locally, and properly configure the Google OAuth credentials.
