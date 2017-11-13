from bot.messages import VK_SECRET_KEY_EXCEPTION_MESSAGE


class VkSecretKeyException(Exception):
    """
    If secret key from current request is not equal
    correct secret key, then exception is raise
    """
    def __init__(self):
        super(VkSecretKeyException, self) \
            .__init__(VK_SECRET_KEY_EXCEPTION_MESSAGE)
