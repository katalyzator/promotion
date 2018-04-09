# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_user_detail(request):
    key = request.POST.get('token')
    user = User.objects.get(auth_token=key)
    print user

    return JsonResponse({
        "username": user.username,
        "firstname": user.first_name
    })
