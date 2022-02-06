from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove

# Reply Keyboards
from aiogram.utils.callback_data import CallbackData

share_location_kb = ReplyKeyboardMarkup()
share_location_kb.add(KeyboardButton("Відправити локацію", request_location=True))

remove_kb = ReplyKeyboardRemove()

# Callback data
input_cb = CallbackData('input', 'type')
verify_cb = CallbackData('verify', 'approval')
flow_cb = CallbackData('flow', 'name')

# Buttons
inline_cancel_btn = InlineKeyboardButton("Відміна", callback_data=flow_cb.new(name='cancel'))

# Inline Keyboards
inline_verify_kb = InlineKeyboardMarkup()
inline_verify_kb.add(InlineKeyboardButton("Підтвердити",
                                          callback_data=verify_cb.new(approval="apply")))
inline_verify_kb.add(InlineKeyboardButton("Відхилити",
                                          callback_data=verify_cb.new(approval="reject")))

inline_flow_choice_kb = InlineKeyboardMarkup()
inline_flow_choice_kb.add(InlineKeyboardButton("Залишив автомобіль",
                                          callback_data=flow_cb.new(name="create_car")))
inline_flow_choice_kb.add(InlineKeyboardButton("Мій автомобіль заблокували",
                                          callback_data=flow_cb.new(name="search_car")))

inline_input_start_kb = InlineKeyboardMarkup()
inline_input_start_kb.add(InlineKeyboardButton("Внести дані",
                                               callback_data=input_cb.new(type="start")))
inline_input_start_kb.add(inline_cancel_btn)

inline_input_phone_kb = InlineKeyboardMarkup()
inline_input_phone_kb.add(InlineKeyboardButton("Додати номер телефону",
                                               callback_data=input_cb.new(type="phone")))
inline_input_phone_kb.add(inline_cancel_btn)

inline_input_car_num_kb = InlineKeyboardMarkup()
inline_input_car_num_kb.add(InlineKeyboardButton("Додати номер автомобіля",
                                                 callback_data=input_cb.new(type="car_number")))
inline_input_car_num_kb.add(inline_cancel_btn)

