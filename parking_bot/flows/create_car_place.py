from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from parking_bot.components import keyboards as kb
from parking_bot.components.keyboards import input_cb, verify_cb
from parking_bot.components.states import NewCarDataState
from parking_bot.flows.base_flow import BaseAutomationFlow


class CreateCarPlaceFlow(BaseAutomationFlow):

    async def start_input(self, query: CallbackQuery, state: FSMContext):
        await query.message.edit_text(
            "Створення нового місця парковки для автомобіля",
            reply_markup=kb.inline_input_start_kb
        )
        await NewCarDataState.start_data_input.set()

    async def phone_number_input(self,  query: CallbackQuery, state: FSMContext):
        await query.message.edit_reply_markup(reply_markup=kb.inline_input_phone_kb)
        await NewCarDataState.phone_number_input.set()

    async def process_phone_number(self, query: CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data["delete_msg"] = query.message.message_id

        await query.message.edit_text("Введіть номер телефону:")

    async def validate_phone_number(self, message: Message, state: FSMContext):
        await message.answer("Цей номер телефону вірний?", reply_markup=kb.inline_verify_kb)
        await message.delete()

        async with state.proxy() as data:
            await self.dp.bot.delete_message(message.from_user.id, data["delete_msg"])

        await NewCarDataState.car_number_input.set()

    async def car_number_input(self, query: CallbackQuery, state: FSMContext):
        await query.message.edit_reply_markup(reply_markup=kb.inline_input_car_num_kb)

    async def process_car_number(self, message: Message, state: FSMContext):
        await message.edit_reply_markup(reply_markup=kb.inline_verify_kb)
        await NewCarDataState.input_data_verify.set()

    async def input_verify(self, message: Message, state: FSMContext):
        await message.edit_text("Автомобіль успішно припарковано!",
                                reply_markup=kb.remove_kb)
        await state.finish()

    async def cancel(self, query: CallbackQuery, state: FSMContext):
        await query.message.edit_text("Оберіть необхідну функцію серед доступних: ",
                                      reply_markup=kb.inline_flow_choice_kb)
        await state.finish()

    def add_handlers(self):
        self.dp.register_callback_query_handler(self.cancel,
                                                kb.flow_cb.filter(name="cancel"),
                                                state="*")
        self.dp.register_callback_query_handler(self.start_input,
                                                kb.flow_cb.filter(name="create_car"))

        self.dp.register_callback_query_handler(self.phone_number_input,
                                                input_cb.filter(type="start"),
                                                state=NewCarDataState.start_data_input)
        self.dp.register_callback_query_handler(self.process_phone_number,
                                                input_cb.filter(type="phone"),
                                                state=NewCarDataState.phone_number_input)
        self.dp.register_message_handler(self.validate_phone_number,
                                         state=NewCarDataState.phone_number_input)

        self.dp.register_callback_query_handler(self.car_number_input,
                                                verify_cb.filter(approval="apply"),
                                                state=NewCarDataState.car_number_input)
        self.dp.register_callback_query_handler(self.process_car_number,
                                                input_cb.filter(type="car_number"),
                                                verify_cb.filter(approval="reject"),
                                                state=NewCarDataState.car_number_input)

        self.dp.register_callback_query_handler(self.input_verify,
                                                verify_cb.filter(approval="apply"),
                                                state=NewCarDataState.input_data_verify)
        self.dp.register_callback_query_handler(self.start_input,
                                                verify_cb.filter(approval="reject"),
                                                state=NewCarDataState.input_data_verify)
