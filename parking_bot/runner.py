from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from parking_bot.flows.commands import CommandsFlow
from parking_bot.flows.create_car_place import CreateCarPlaceFlow
from parking_bot.flows.user_location import LocationDataFlow


class BotRunner:

    def __init__(self, token: str):
        self.bot = Bot(token=token)
        self.storage = MemoryStorage()
        self.dp = Dispatcher(bot=self.bot, storage=self.storage)

    def setup(self):
        # user_tracker_middleware = None
        # self.dp.setup_middleware(user_tracker_middleware)
        CommandsFlow(self.dp).add_handlers()
        LocationDataFlow(self.dp).add_handlers()

        CreateCarPlaceFlow(self.dp).add_handlers()

    def run_bot(self):
        executor.start_polling(self.dp)

