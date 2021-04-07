from django import forms

class RequestForm(forms.Form):
    # url = forms.URLField()
    url = forms.CharField(max_length=255, label='URL:')
