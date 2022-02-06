from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from parking_bot.components import keyboards
from parking_bot.flows.base_flow import BaseAutomationFlow


class CommandsFlow(BaseAutomationFlow):

    async def start_handler(self, message: Message, state: FSMContext):
        await message.answer("START!")

    async def help_handler(self, message: Message):
        pass

    async def location_handler(self, message: Message):
        await message.answer('Надішліть локацію:', reply_markup=keyboards.share_location_kb)

    async def cancel_handler(self, *args, state: FSMContext, **kwargs):
        await state.finish()

    def add_handlers(self):
        self.dp.register_message_handler(self.start_handler, commands=["start"])
        self.dp.register_message_handler(self.help_handler, commands=["help"])
        self.dp.register_message_handler(self.location_handler, commands=["location"])

        self.dp.register_message_handler(self.cancel_handler, commands=["cancel"])
