import telebot
import settings
import sqlite3
import datetime
import menu
import text
import logic
from random import choice
from string import ascii_uppercase
#**********************************************************************************************************************
def start_bot():

    bot = telebot.TeleBot(settings.BOT_TOKEN)
#**********************************************************************************************************************
    @bot.message_handler(commands=['start'])
    def start(message):
        if message.from_user.username != None:
            conn = sqlite3.connect('base_pyramid.sqlite')
            cursor = conn.cursor()

            cursor.execute(f'SELECT * FROM access WHERE user_id = "{message.chat.id}"')
            row = cursor.fetchall()

            if len(row) == 0:
                cursor.execute(f'SELECT * FROM users WHERE user_id = "{message.chat.id}"')
                row = cursor.fetchall()

                if len(row) == 0:

                    cursor.execute(f'INSERT INTO users VALUES ("{message.chat.id}", "{message.from_user.username}", "{datetime.datetime.now()}", "no")')
                    
                    conn.commit()
                
                    bot.send_message(chat_id=message.chat.id,
                                 text=text.about_company,
                                 reply_markup=menu.menu_start)
                if len(row) > 0:
                    cursor.execute(f'SELECT * FROM access WHERE user_id = "{message.chat.id}"')
                    cursor.execute(f'UPDATE users SET login = "{message.from_user.username}" WHERE user_id = "{message.chat.id}"')
                    bot.send_message(chat_id=message.chat.id,
                                 text=text.about_company,
                                 reply_markup=menu.menu_start)
            else:
                cursor.execute(f'SELECT * FROM access WHERE user_id = "{message.chat.id}"')
                cursor.execute(f'UPDATE users SET login = "{message.from_user.username}" WHERE user_id = "{message.chat.id}"')
                bot.send_message(chat_id=message.chat.id,
                             text=text.start_menu.format(name=message.from_user.first_name, id=message.chat.id),
                             reply_markup=menu.menu_main)
        else:
           bot.send_message(chat_id=message.chat.id,
                             text='Введите username в настройках телеграма для регистрации')
#**********************************************************************************************************************
    @bot.message_handler(commands=['admin'])
    def admin(message):
        if str(message.chat.id) == settings.ADMIN_ID:
            bot.send_message(chat_id=message.chat.id,
                             text=text.admin_menu.format(name=message.from_user.first_name),
                             reply_markup=menu.menu_admin)
#**********************************************************************************************************************
    @bot.callback_query_handler(func=lambda call: True)
    def handler_call(call):
        conn = sqlite3.connect('base_pyramid.sqlite')
        cursor = conn.cursor()
        
        chat_id = call.message.chat.id #И user_id
        message_id = call.message.message_id
        
        if call.data == 'new':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.access_no_info,
                                  reply_markup=menu.menu_next)
        
        if call.data == 'no_new':
            cursor.execute(f'INSERT INTO access VALUES ("{chat_id}")')
            conn.commit()
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.access_yes_info,
                                  reply_markup=menu.menu_main)
                                  
        
#**********************************************************************************************************************
    bot.polling(none_stop=True)

start_bot()