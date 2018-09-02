# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts               import redirect

'''
def index(request):
    #return HttpResponse("Hello, world. You're at the papersdb index.")
    return render(request, 'appa/index.html', {})
'''

def index(request): 
    user = request.user
    print dir(user)

    if user.is_authenticated():
        return render(request, 'index.html', {user:user})
    else:
        redirect_url = "http://" + request.get_host() + "/accounts/login/"
        return redirect(redirect_url)

    # this is your new view
    return render(request, 'index.html')
