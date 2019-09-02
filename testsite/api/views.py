from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse

from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.core import serializers
import json

from django.contrib import messages
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt

# [Django: import auth user to the model](https://stackoverflow.com/questions/12921789/django-import-auth-user-to-the-model)
from django.apps import apps
from django.contrib.auth.models import User


Profile = apps.get_model('testapp', 'Profile')
Message = apps.get_model('testapp', 'Message')


def login_action(request):
    context = {}

    username = request.GET['username']
    password = request.GET['password']

    user = authenticate(username=username, password=password)

    response_data = {}

    if user:
        login(request, user)
        response_data['user_id'] = user.id
        response_data['username'] = username
        return JsonResponse(response_data, status=200)
    else:
        response_data['error'] = 'User authentication failed. Please check again!'
        return JsonResponse(response_data, status=403)


def logout_action(request):
    logout(request)
    return redirect(reverse('login'))


def signup_action(request):
    context = {}

    if request.method == 'GET':
        context['form'] = SignupForm()
        return render(request, 'testapp/signup.html', context)

    form = SignupForm(request.POST)
    context['form'] = form

    if not form.is_valid():
        return render(request, 'testapp/signup.html', context)

    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()
    # also create a new profile for the newly registered user
    Profile.objects.create(user=new_user)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
    login(request, new_user)

    return redirect(reverse('home'))


def error(request):
    return HttpResponse("Sorry, but this page isn't available...")
