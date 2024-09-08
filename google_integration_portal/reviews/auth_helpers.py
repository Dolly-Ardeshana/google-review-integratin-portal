# reviews/auth_helpers.py

import os
from google_auth_oauthlib.flow import Flow
from django.conf import settings

def get_google_oauth_flow():
    flow = Flow.from_client_config(
        client_config={
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "redirect_uris": [settings.GOOGLE_REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=settings.GOOGLE_SCOPES,
    )
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI

    # Allow HTTP if running locally
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    return flow
