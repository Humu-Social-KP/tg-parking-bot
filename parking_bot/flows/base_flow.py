from aiogram import Dispatcher


class BaseAutomationFlow:

    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def add_handlers(self):
        raise NotImplementedError()
