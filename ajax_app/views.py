from django.shortcuts import render
from django.http import JsonResponse
from .forms import RequestForm, PostForm
import requests
import json

# Create your views here.


def home(request):
    form = RequestForm()
    post_form = PostForm()
    return render(request, 'ajax_app/home.html', {'form': form, 'postform': post_form})

def api_request(request):
    request_form = RequestForm(request.GET)
    if request_form.is_valid():
        odp = requests.get(request_form.cleaned_data['url'])
        return JsonResponse({'result': odp.text})
    return JsonResponse({'result': 'Not working!'})

def post_api_request(request):
    if request.is_ajax():
        if request.method == 'POST':
            # t = 'Raw Data: "%s"' % request.body
            t = 'Raw Data: "%s"' % request.POST['value1']
            # x =  '{ "myval1": ' + request.POST["value1"] + ' , "myval2": ' + request.POST["value2"] + ', "myval3":' + request.POST["value3"] + '}'
            x =  {'myval1': request.POST['value1'], 'myval2': request.POST['value2'], 'myval3': request.POST['value3']}
            y = json.dumps(x)
            r = requests.post(request.POST['url'], data = x)
            print('Raw Data: "%s"' % request.POST['value1'])
            print(type(x))
            # return JsonResponse({'result': x})
            return JsonResponse(x, safe=False)
    return JsonResponse({'result': 'Not working!!'})
