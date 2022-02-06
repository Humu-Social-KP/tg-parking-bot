from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from parking_bot.components import keyboards
from parking_bot.components.states import NewCarDataState, SearchCarOwnerState
from parking_bot.flows.base_flow import BaseAutomationFlow


class LocationDataFlow(BaseAutomationFlow):

    async def process_location_data(self, message: Message, state: FSMContext):
        await message.answer(f'{message.location.latitude}:{message.location.longitude}')
        await message.answer("Оберіть дію:",
                             reply_markup=keyboards.inline_flow_choice_kb)

    async def process_create(self, query: CallbackQuery, state: FSMContext):
        await query.message.delete()
        await NewCarDataState.start_data_input.set()

    async def process_search(self, query: CallbackQuery, state: FSMContext):
        await query.message.delete()
        await SearchCarOwnerState.start_data_input.set()

    def add_handlers(self):
        self.dp.register_message_handler(self.process_location_data,
                                         content_types=[types.ContentType.LOCATION])
