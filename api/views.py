from django.shortcuts import render_to_response
from django.http.response import HttpResponse
import json

# Create your views here.

def login(request):
    if request.method=='POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        result['username'] = "["+username+"]"
        result['password'] = "["+password+"]"
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    if request.method=='GET':
        result = {}
        username = request.GET.get('username')
        password = request.GET.get('password')
        # print(username,password)
        result['username']="["+username+"]"
        result['password'] ="["+password+"]"
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')