import vk_api

from django.http import HttpResponse

from bot.exceptions.RedundantBotAnswerException import RedundantBotAnswerException
from bot.messages import NOT_SUBSCRIBED_MESSAGE, \
    GROUP_JOIN_MESSAGE, GROUP_LEAVE_MESSAGE, GROUP_OFFICERS_EDIT_MESSAGE

from vk_bot_template.settings import vk_session, \
    INTEGER_GROUP_ID, VK_CONFIRMATION_TOKEN, BOT_OWNER_USER_ID


class BotFunctions:
    def __init__(self, user_id, message_handler):
        self.user_id = user_id
        self.message_handler = message_handler
        self.functions = {
            'confirmation': lambda: HttpResponse(VK_CONFIRMATION_TOKEN),
            'message_new': self.__message_new_func,
            'group_join': self.__group_join_func,
            'group_leave': self.__group_leave_func,
            'group_officers_edit': self.__group_officers_edit_func
        }

    def do(self, func_type):
        return self.functions.get(func_type)()

    def __message_new_func(self):
        try:
            last_msg = vk_session.method('messages.getHistory',
                                         {'peer_id': self.user_id, 'count': 1})
            if last_msg['items'][0]['from_id'] == -INTEGER_GROUP_ID:
                raise RedundantBotAnswerException()

            vk_session.method('messages.setActivity',
                              {'user_id': self.user_id, 'type': 'typing'})
        except RedundantBotAnswerException:
            return HttpResponse('ok', 200)
        except vk_api.VkApiError:
            pass  # ignore, as setActivity and redundancy answer check is not vital

        self.message_handler.send_answer()
        if not vk_session.method('groups.isMember',
                                 {'group_id': INTEGER_GROUP_ID, 'user_id': self.user_id}):
            self.message_handler.send_message(NOT_SUBSCRIBED_MESSAGE)

        return HttpResponse('ok', 200)

    def __group_join_func(self):
        self.message_handler.send_message(message=GROUP_JOIN_MESSAGE)
        return HttpResponse('ok', 200)

    def __group_leave_func(self):
        self.message_handler.send_message(message=GROUP_LEAVE_MESSAGE)
        return HttpResponse('ok', 200)

    def __group_officers_edit_func(self):
        self.message_handler.send_message(
            message=GROUP_OFFICERS_EDIT_MESSAGE,
            user_id=BOT_OWNER_USER_ID
        )
        return HttpResponse('ok', 200)
