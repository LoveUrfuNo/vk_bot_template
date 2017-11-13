from bot.exceptions import VkSecretKeyException

from vk_bot_template.settings import vk_session, VK_SECRET_KEY


class MessageHandler:
    def __init__(self, user_id, user_message, secret_key):
        if secret_key != VK_SECRET_KEY:
            raise VkSecretKeyException

        self.vk_session = vk_session
        self.user_id = user_id
        self.user_message = user_message

    def send_message(self, message, user_id=None, attachment=''):
        user_id = self.user_id if user_id is None else user_id
        vk_session.method('messages.send', {
            'user_id': user_id,
            'message': message,
            'attachment': attachment
        })

    def send_answer(self):
        message_to_send = self.__get_answer(self.user_message)
        self.send_message(message_to_send)

    def __get_answer(self, user_message):
        # TODO: write your code here
        return 'message_to_user'
