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
menu_information = types.InlineKeyboardMarkup(row_width=1)
menu_information.add(
    types.InlineKeyboardButton(text='Продуктовая линейка', callback_data='product_line'),
    types.InlineKeyboardButton(text='Информация о компании', callback_data='company_information'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_main_menu'),
)
menu_back_to_information = types.InlineKeyboardMarkup(row_width=2)
menu_back_to_information.add(
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu_information')
)
#***************************************************************************************************
menu_knowelege_base = types.InlineKeyboardMarkup(row_width=2)
menu_knowelege_base.add(
    types.InlineKeyboardButton(text='Общая информация', callback_data='out_information'),
    types.InlineKeyboardButton(text='Кухня', callback_data='citchen_information'),
    types.InlineKeyboardButton(text='Техника безопасности', callback_data='safety_information'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_main_menu')
)
menu_safety_information = types.InlineKeyboardMarkup(row_width=2)
menu_safety_information.add(
    types.InlineKeyboardButton(text='ТБ на кухне', callback_data='safety_information_citchen'),
    types.InlineKeyboardButton(text='При пожаре', callback_data='safety_information_fire'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_knowelege_base_menu')
)
menu_out_information = types.InlineKeyboardMarkup(row_width=2)
menu_out_information.add(
    types.InlineKeyboardButton(text='Зоны', callback_data='zones_information'),
    types.InlineKeyboardButton(text='Дресс-код', callback_data='dress_code_information'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_knowelege_base_menu')
)
menu_citchen_information = types.InlineKeyboardMarkup(row_width=2)
menu_citchen_information.add(
    types.InlineKeyboardButton(text='Идеальная пицца', callback_data='perfect_pizza_information'),
    types.InlineKeyboardButton(text='Линия начинения', callback_data='line_information'),
    types.InlineKeyboardButton(text='Маркировка', callback_data='markup_information'),
    types.InlineKeyboardButton(text='Мойка', callback_data='clean_information'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_knowelege_base_menu')
)
#***************************************************************************************************
menu_back_to_citchen_information = types.InlineKeyboardMarkup(row_width=1)
menu_back_to_citchen_information.add(
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_citchen_information')
)
menu_back_to_out_information = types.InlineKeyboardMarkup(row_width=1)
menu_back_to_out_information.add(
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_out_information')
)
menu_back_to_safety_information = types.InlineKeyboardMarkup(row_width=1)
menu_back_to_safety_information.add(
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_safety_information')
)
#*****************Тесты*****************************************************************************