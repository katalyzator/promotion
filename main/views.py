# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from main.models import *

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_user_detail(request):
    key = request.POST.get('token')
    user = User.objects.get(auth_token=key)

    return JsonResponse({
        "username": user.username,
        "email": user.email,
        "phone_number": user.phone_number,
        "avatar": (u"{}{}{}".format("http://", request.get_host(), user.image.url)).encode(
            "utf-8") if user.image else None,
        "company_status": user.company_status

    })
