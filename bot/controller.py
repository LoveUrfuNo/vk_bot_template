# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import traceback

from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bot.classes.BotFunctions import BotFunctions
from bot.classes.MessageHandler import MessageHandler

from vk_bot_template import settings


@csrf_exempt
def controller(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body.decode('utf-8'))
            user_id = request_data['object']['user_id']
            message_handler = MessageHandler(
                user_id,
                user_message=request_data['object']['body'],
                secret_key=request_data['secret']
            )

            if 'type' not in request_data.keys():
                send_mail('Request not from vk.com',
                          'Request body: ' + str(request),
                          settings.EMAIL_HOST_USER,
                          [settings.EMAIL_HOST_USER])
                return HttpResponse('not vk')
            else:
                return BotFunctions(user_id, message_handler) \
                    .do(func_type=request_data['type'])

        except Exception as exc:
            send_mail('ERROR',
                      str(exc) + "\n\n" + traceback.format_exc(),
                      settings.EMAIL_HOST_USER,
                      [settings.EMAIL_HOST_USER])

            return HttpResponse('ok', 200)


# {"type":"message_new","object":{"id":426981,"date":1510497760,"out":0,"user_id":124696222,"read_state":0,"title":"","body":"Привет,не игнорь"},"group_id":149749558,"secret":"CkJwBaVQHaLU8S9WhQFw3DgxN4DKxQP7h"}
