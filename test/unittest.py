from parking_bot.flows.create_car_place import *
from parking_bot.settings import *
from aiogram import Bot, Dispatcher
from unittest import IsolatedAsyncioTestCase
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class TestBot(IsolatedAsyncioTestCase):

    async def TestStartInput(self):
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher(bot)
        flow = CreateCarPlaceFlow(dp)
        state = FSMContext(chat="", storage=MemoryStorage(), user="")  # chat and user ids?
        expected_state = NewCarDataState.start_data_input
        await flow.start_input(input_cb.new(type="start"), state)
        self.assertEqual(expected_state, NewCarDataState.start_data_input.state)
