from django import forms

class GetUserLinkForm(forms.Form):
    link = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'url',
        'id' : 'original-url',
        'name' : 'original-url',
        'placeholder' : 'https://example.com'
    }))