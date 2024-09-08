from django import forms

class ReplyForm(forms.Form):
    review_id = forms.CharField(widget=forms.HiddenInput())  # Hidden field to store the review ID
    reply_text = forms.CharField(
        label='Your Reply',
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your reply here...'}),
        max_length=4096  # The maximum length of a reply in Google My Business is 4096 characters
    )
