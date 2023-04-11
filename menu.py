from telebot import types

menu_access_no = types.InlineKeyboardMarkup(row_width=3)
menu_access_no.add(
    types.InlineKeyboardButton(text='ТЕСТ(нет доступа)', callback_data='test_no_access') 
)

menu_access_yes = types.InlineKeyboardMarkup(row_width=2)
menu_access_yes.add(
    types.InlineKeyboardButton(text='ТЕСТ(есть доступ)', callback_data='test_yes_access')
)

menu_admin = types.InlineKeyboardMarkup(row_width=2)
menu_admin.add(
    types.InlineKeyboardButton(text='ТЕСТ(админ)', callback_data='admin')
)

btn_back_no_access = types.InlineKeyboardMarkup(row_width=3)
btn_back_no_access.add(
    types.InlineKeyboardButton(text='❌', callback_data='back_2')
)

functions_access_no = types.InlineKeyboardMarkup(row_width=3)
functions_access_no.add(
    types.InlineKeyboardButton(text='def1(no access)', callback_data='def_test'),
    types.InlineKeyboardButton(text='❌', callback_data='back')
)
