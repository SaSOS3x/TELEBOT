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

#*****************************************************************************************************

menu_main = types.InlineKeyboardMarkup(row_width=2)
menu_main.add(
    types.InlineKeyboardButton(text='Профиль', callback_data='profile'),
    types.InlineKeyboardButton(text='О компании', callback_data='information'),
    types.InlineKeyboardButton(text='Обучение', callback_data='learning'),
    types.InlineKeyboardButton(text='База знаний', callback_data='knowelege_base')
)
menu_start = types.InlineKeyboardMarkup(row_width=2)
menu_start.add(
    types.InlineKeyboardButton(text='Я новый сотрудник', callback_data='new'),
    types.InlineKeyboardButton(text='Я уже работаю', callback_data='no_new')
)
menu_next = types.InlineKeyboardMarkup(row_width=2)
menu_next.add(
    types.InlineKeyboardButton(text='Пиццемейкер', callback_data='pizza_maker'),
    types.InlineKeyboardButton(text='Кассир', callback_data='cassier'),
    types.InlineKeyboardButton(text='Инструктор', callback_data='instructor'),
    types.InlineKeyboardButton(text='Менеджер', callback_data='manager')
)
start_new_worker = types.InlineKeyboardMarkup(row_width=2)
start_new_worker.add(
    types.InlineKeyboardButton(text='Стать новым сотрудником', callback_data='new_worker'),
)