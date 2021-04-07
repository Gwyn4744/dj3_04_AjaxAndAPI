from django.shortcuts import render
from django.http import JsonResponse
from .forms import RequestForm
import requests

# Create your views here.


def home(request):
    form = RequestForm()
    return render(request, 'ajax_app/home.html', {'form': form})

def api_request(request):
    request_form = RequestForm(request.GET)
    if request_form.is_valid():
        odp = requests.get(request_form.cleaned_data['url'])
        return JsonResponse({'result': odp.text})
    return JsonResponse({'result': 'Not working!'})
