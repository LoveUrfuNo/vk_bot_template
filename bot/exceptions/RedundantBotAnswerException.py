from bot.messages import REDUNDANT_ANSWER_EXCEPTION_MESSAGE


class RedundantBotAnswerException(Exception):
    """
    If last dialog message send from our bot,
    then we dont need answer again
    """
    def __init__(self):
        super(RedundantBotAnswerException, self) \
            .__init__(REDUNDANT_ANSWER_EXCEPTION_MESSAGE)
