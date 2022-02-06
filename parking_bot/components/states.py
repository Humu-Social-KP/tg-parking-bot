from aiogram.dispatcher.filters.state import StatesGroup, State


class NewCarDataState(StatesGroup):
    start_data_input = State()
    phone_number_input = State()
    car_number_input = State()
    input_data_verify = State()


class SearchCarOwnerState(StatesGroup):
    start_data_input = State()
    car_number_input = State()
    car_number_verify = State()
    search_results = State()


