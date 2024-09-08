
# Create your views here.


from django.shortcuts import render, redirect
from googleapiclient.discovery import build
from .auth_helpers import get_google_oauth_flow
from google.oauth2.credentials import Credentials
from .forms import ReplyForm
from django.http import HttpResponse
from googleapiclient.errors import HttpError


def login(request):
    # Create the OAuth2.0 flow object
    flow = get_google_oauth_flow()
    # Generate authorization URL and state
    authorization_url, state = flow.authorization_url(prompt='consent')
    
    # Save the state in the session
    request.session['state'] = state
    
    # Redirect to Google's OAuth 2.0 server
    return redirect(authorization_url)

def oauth2callback(request):
    # Check if 'state' is in session to prevent KeyError
    if 'state' not in request.session:
        return redirect('login')  # Redirect to login if 'state' is not in session
    
    # Retrieve the state from the session
    state = request.session['state']
    
    # Create the OAuth2.0 flow object with the state
    flow = get_google_oauth_flow()
    flow.fetch_token(authorization_response=request.build_absolute_uri())

    # Save credentials in the session
    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)

    return redirect('index')

def index(request):
    # Check if credentials exist in session
    if 'credentials' not in request.session:
        return redirect('login')

    # Load credentials from session
    credentials = Credentials(**request.session['credentials'])

    # Use the correct API name and version
    service = build('mybusinessaccountmanagement', 'v1', credentials=credentials)

    # Fetch the list of accounts
    accounts = service.accounts().list().execute()
    
    # Assuming you want to fetch reviews from the first account
    account_id = accounts['accounts'][0]['name']

    # Use the correct API name for fetching reviews
    review_service = build('mybusinessbusinessinformation', 'v1', credentials=credentials)
    reviews = review_service.accounts().locations().reviews().list(parent=account_id).execute()

    # Pass the reviews and an empty form to the template
    form = ReplyForm()
    return render(request, 'reviews/index.html', {'reviews': reviews.get('reviews', []), 'form': form})

def reply_to_review(request):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            credentials = Credentials(**request.session['credentials'])
            review_id = form.cleaned_data['review_id']
            reply_text = form.cleaned_data['reply_text']

            try:
                # Initialize the My Business API client
                service = build('mybusinessbusinessinformation', 'v1', credentials=credentials)

                # Construct the parent resource name for the review reply
                parent = f"{review_id}/reply"

                # Create the reply
                reply_body = {
                    'comment': reply_text
                }

                # Call the API to create a reply to the review
                response = service.accounts().locations().reviews().reply(name=parent, body=reply_body).execute()
                return redirect('index')  # Redirect to the index page after a successful reply

            except HttpError as e:
                return HttpResponse(f"An error occurred while replying to the review: {e}")
    else:
        return redirect('index')  # Redirect to index if the request method is not POST

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }