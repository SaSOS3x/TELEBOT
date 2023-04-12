import telebot
import settings
import sqlite3
import datetime
import menu
import text
import logic
from random import choice
from string import ascii_uppercase
import os
#**********************************************************************************************************************

puff = os.getcwd()
os.chdir('..')
conn = sqlite3.connect('base_pyramid.db', check_same_thread=False)
cursor = conn.cursor()
os.chdir(puff)

def start_bot():
    
    bot = telebot.TeleBot(settings.BOT_TOKEN)
    
#**********************************************************************************************************************
    @bot.message_handler(commands=['start'])
    def start(message):
        if message.from_user.username != None:
            
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


                cursor.execute(f'SELECT * FROM users WHERE user_id = "{message.chat.id}"')
                name = cursor.fetchone()[4]
                if name == 'none':
                    clas = f'Ваша должность: нету должности\n\n'\
                       'Чтобы получить должность, подойдите к директору вашего учереждения и попросите его выдать вам должность'
                else:
                    clas = f'Ваша должность: {name}'
                bot.send_message(chat_id=message.chat.id,
                                  text='Вы находитесь в главном меню\n\n'\
                                       f'Ваш индетификатор внутри системы: "{message.chat.id}"\n'
                                       + clas,
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
        
        chat_id = call.message.chat.id #И user_id
        message_id = call.message.message_id
        
        if call.data == 'new':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.new_worker,
                                  reply_markup=menu.menu_next)
        
        if call.data == 'no_new':
            cursor.execute(f'INSERT INTO access VALUES ("{chat_id}")')
            conn.commit()
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.access_yes_info,
                                  reply_markup=menu.menu_main)
            
        if call.data == 'pizza_maker':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.about_pizzamaker)
            bot.send_message(chat_id=chat_id,
                             text='Твой дресс-код:\n\n' + text.pizzamaker_stuff)
            bot.send_message(chat_id=chat_id,
                             text=text.about_help)
            bot.send_message(chat_id=chat_id,
                                  text=text.about_bot,
                                  reply_markup=menu.start_new_worker)
            
        if call.data == 'cassier':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.about_cassir)
            bot.send_message(chat_id=chat_id,
                             text='Твой дресс-код:\n\n' + text.cassier_stuff)
            bot.send_message(chat_id=chat_id,
                             text=text.about_help)
            bot.send_message(chat_id=chat_id,
                                  text=text.about_bot,
                                  reply_markup=menu.start_new_worker)
            
        if call.data == 'instructor':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.about_teacher)
            bot.send_message(chat_id=chat_id,
                             text='Твой дресс-код:\n\n' + text.teacher_stuff)
            bot.send_message(chat_id=chat_id,
                             text=text.about_help)
            bot.send_message(chat_id=chat_id,
                                  text=text.about_bot,
                                  reply_markup=menu.start_new_worker)

        if call.data == 'manager':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.about_manager)
            bot.send_message(chat_id=chat_id,
                             text='Твой дресс-код:\n\n' + text.manager_stuff)
            bot.send_message(chat_id=chat_id,
                             text=text.about_help)
            bot.send_message(chat_id=chat_id,
                                  text=text.about_bot,
                                  reply_markup=menu.start_new_worker)
#***********************************************************************************
        if call.data == 'new_worker':
            cursor.execute(f'INSERT INTO access VALUES ("{chat_id}")')
            conn.commit()
            cursor.execute(f'SELECT * FROM users WHERE user_id = "{chat_id}"')
            name = cursor.fetchone()[4]
            if name == 'none':
                clas = f'Ваша должность: нету должности\n\n'\
                       'Чтобы получить должность, подойдите к директору вашего учереждения и попросите его выдать вам должность'
            else:
                clas = f'Ваша должность: {name}'
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text='Вы находитесь в главном меню\n\n'\
                                       f'Ваш индетификатор внутри системы: "{chat_id}"\n'
                                       + clas,
                                  reply_markup=menu.menu_main)
#***********************************************************************************        
        if call.data == 'information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text='',
                                  

            )
        if call.data == 'product_line':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text='',
                                  

            )
        if call.data == 'company_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text='',
                                  

            )
        if call.data == 'back_to_main_menu':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text='',
                                  

            )
        



        
                                  
        
#**********************************************************************************************************************
    bot.polling(none_stop=True)

start_bot()