from django import forms

class RequestForm(forms.Form):
    # url = forms.URLField()
    url = forms.CharField(max_length=255, label='URL:')

class PostForm(forms.Form):
    purl = forms.CharField(max_length=255, label='URL:')
    val1 = forms.CharField(max_length=255, label='Val1:')
    val2 = forms.CharField(max_length=255, label='Val2:')
    val3 = forms.CharField(max_length=255, label='Val3:')
