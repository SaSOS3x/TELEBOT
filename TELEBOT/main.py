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
                    cursor.execute(f'INSERT INTO class VALUES ("{message.chat.id}", "none")')
                    cursor.execute(f'INSERT INTO courses VALUES ("{message.chat.id}", "0", "0", "0", "0", "0", "0")')
                    cursor.execute(f'INSERT INTO lvl VALUES ("{message.chat.id}", "0")')
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


                cursor.execute(f'SELECT * FROM class WHERE user_id = "{message.chat.id}"')
                name = cursor.fetchone()[1]
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
#***ВводныйИнструктаж*******************************************************************************************************************
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
            cursor.execute(f'UPDATE lvl SET lvl = "2" WHERE user_id = "{call.message.chat.id}"')
            cursor.execute(f'INSERT INTO access VALUES ("{chat_id}")')
            conn.commit()
            cursor.execute(f'SELECT * FROM class WHERE user_id = "{call.message.chat.id}"')
            name = cursor.fetchone()[1]
            if name == 'none':
                clas = f'Ваша должность: нету должности\n\n'\
                    'Чтобы получить должность, подойдите к директору вашего учереждения и попросите его выдать вам должность'
            else:
                clas = f'Ваша должность: {name}'
            bot.send_message(chat_id=call.message.chat.id,
                                  text='Вы находитесь в главном меню\n\n'\
                                       f'Ваш индетификатор внутри системы: "{call.message.chat.id}"\n'
                                       + clas,
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
#*******НовыйРаботник****************************************************************************
        if call.data == 'new_worker':
            cursor.execute(f'INSERT INTO access VALUES ("{chat_id}")')
            conn.commit()
            cursor.execute(f'SELECT * FROM class WHERE user_id = "{chat_id}"')
            name = cursor.fetchone()[1]
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
                
#*******Информация****************************************************************************
               
        if call.data == 'information':
            msg = bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.information + text.about_help,
                                  reply_markup=menu.menu_information) 
            
        if call.data == 'product_line':
            #bot.delete_message(chat_id=chat_id,message_id=msg.message_id)
            bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
            p = open('img/pizzes.png', 'rb')
            bot.send_photo(chat_id=chat_id, photo=p,
                           caption=text.company_product_line,
                           reply_markup=menu.menu_back_to_information)

        if call.data == 'company_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.company_history,
                                  reply_markup=menu.menu_back_to_information)
                                  
        if call.data == 'back_to_menu_information':
            bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
            bot.send_message(chat_id=chat_id,
                                  text=text.information,
                                  reply_markup=menu.menu_information)
            
        if call.data == 'back_to_main_menu':
            cursor.execute(f'SELECT * FROM class WHERE user_id = "{chat_id}"')
            name = cursor.fetchone()[1]
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
#********БазаЗнаний***************************************************************************        
        if call.data == 'knowelege_base':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.knowelege_base,
                                  reply_markup=menu.menu_knowelege_base)
        
        if call.data == 'out_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.out_information_text,
                                  reply_markup=menu.menu_out_information)
        
        if call.data == 'citchen_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.citchen_information_text,
                                  reply_markup=menu.menu_citchen_information)
        
        if call.data == 'safety_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.safety_information_text,
                                  reply_markup=menu.menu_safety_information)
        
        if call.data == 'back_to_knowelege_base_menu':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.knowelege_base,
                                  reply_markup=menu.menu_knowelege_base)
#********out_information*************************************************************************************************************         
        if call.data == 'zones_information':
            bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
            p = open('img/company.png', 'rb')
            bot.send_photo(chat_id=chat_id,
                                  photo=p,
                                  caption=text.base_information_zones,
                                  reply_markup=menu.menu_back_to_out_information)
            
        if call.data == 'dress_code_information':
            bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
            bot.send_message(chat_id=chat_id,
                                  text=text.dress_code_information_text,
                                  reply_markup=menu.menu_back_to_out_information)
            
        if call.data == 'back_to_out_information':
            bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
            bot.send_message(chat_id=chat_id,
                                  text=text.out_information_text,
                                  reply_markup=menu.menu_out_information)
#********citchen_information*************************************************************************************************************
        if call.data == 'perfect_pizza_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.perfect_pizza_information_text,
                                  reply_markup=menu.menu_back_to_citchen_information)
        
        if call.data == 'line_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.line_information_text,
                                  reply_markup=menu.menu_back_to_citchen_information)
        
        if call.data == 'markup_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.markup_information_text,
                                  reply_markup=menu.menu_back_to_citchen_information)
        
        if call.data == 'clean_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.clean_information_text,
                                  reply_markup=menu.menu_back_to_citchen_information)
            
        if call.data == 'back_to_citchen_information':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.citchen_information_text,
                                  reply_markup=menu.menu_citchen_information)
#********safety_information*************************************************************************************************************
        if call.data == 'safety_information_citchen':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.safety_information_citchen_text,
                                  reply_markup=menu.menu_back_to_safety_information)
        
        if call.data == 'safety_information_fire':
            bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
            p = open('img/evacuation.png', 'rb')
            bot.send_photo(chat_id=chat_id,
                                  photo=p,
                                  caption=text.safety_information_fire,
                                  reply_markup=menu.menu_back_to_safety_information)
            
        if call.data == 'back_to_safety_information':
            bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
            bot.send_message(chat_id=chat_id,
                                  text=text.safety_information_text,
                                  reply_markup=menu.menu_safety_information)
#********Обучение*************************************************************************************************************
        if call.data == 'learning':
            cursor.execute(f'SELECT * FROM lvl WHERE user_id = "{chat_id}"')
            lvl = cursor.fetchone()[1]
            if lvl == '0':
                bot.edit_message_text(chat_id=chat_id,
                                      message_id=message_id,
                                  text=text.learning_text,
                                  reply_markup=menu.menu_learning_lvl0)
            elif lvl == '1':
                bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.learning_text,
                                  reply_markup=menu.menu_learning_lvl1)
            else:
                bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.learning_text,
                                  reply_markup=menu.menu_learning_lvl2)
                
        if call.data == 'test_safety_instruction':
            msg = bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.test_safety_instruction_text_1)
            bot.register_next_step_handler(msg, test_1_stage_1)

        if call.data == 'test_company':
            msg = bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.test_company_text_1)
            bot.register_next_step_handler(msg, test_2_stage_1)

        if call.data == 'test_pizzamaker':
            msg = bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.test_pizzamaker_text_1)
            bot.register_next_step_handler(msg, test_pizza_stage_1)

        if call.data == 'test_cassier':
            msg = bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.test_cassier_text_1)
            bot.register_next_step_handler(msg, test_cassier_stage_1)

        if call.data == 'test_manager':
            msg = bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.test_manager_text_1)
            bot.register_next_step_handler(msg, test_manager_stage_1)

        if call.data == 'test_teacher':
            msg = bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.test_teacher_text_1)
            bot.register_next_step_handler(msg, test_teacher_stage_1)

        if call.data == 'back_to_learning_menu':
            cursor.execute(f'SELECT * FROM lvl WHERE user_id = "{chat_id}"')
            lvl = cursor.fetchone()[1]
            if lvl == '0':
                bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.learning_text,
                                  reply_markup=menu.menu_learning_lvl0)
            elif lvl == '1':
                bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.learning_text,
                                  reply_markup=menu.menu_learning_lvl1)
            else:
                bot.edit_message_text(chat_id=chat_id,
                                 message_id=message_id,
                                  text=text.learning_text,
                                  reply_markup=menu.menu_learning_lvl2)
                
#********Обучение*************************************************************************************************************

    def test_1_stage_1(message):
        if message.text == '1':
            answer1 = '1'
        else:
            answer1 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_safety_instruction_text_2)
        bot.register_next_step_handler(msg, test_1_stage_2, answer1)
    def test_1_stage_2(message, answer1):
        if message.text == '1':
            answer2 = '1'
        else:
            answer2 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_safety_instruction_text_3)
        bot.register_next_step_handler(msg, test_1_stage_3, answer1, answer2)
    def test_1_stage_3(message, answer1, answer2):
        if message.text == '1':
            answer3 = '0'
        else:
            answer3 = '1'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        if (answer1 + answer2 + answer3) == '111':
            cursor.execute(f'UPDATE lvl SET lvl = "1" WHERE user_id = "{message.chat.id}"')
            cursor.execute(f'UPDATE courses SET safety = "Сдал" WHERE user_id = "{message.chat.id}"')
            conn.commit()
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_won,
                                  reply_markup=menu.menu_back_to_learning_menu)
        else:
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_defeat,
                                  reply_markup=menu.menu_back_to_learning_menu)
            
    def test_2_stage_1(message):
        if message.text == '1':
            answer1 = '1'
        else:
            answer1 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_company_text_2)
        bot.register_next_step_handler(msg, test_2_stage_2, answer1)
    def test_2_stage_2(message, answer1):
        if message.text == '1':
            answer2 = '1'
        else:
            answer2 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_company_text_3)
        bot.register_next_step_handler(msg, test_2_stage_3, answer1, answer2)
    def test_2_stage_3(message, answer1, answer2):
        if message.text == '1':
            answer3 = '0'
        else:
            answer3 = '1'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        if (answer1 + answer2 + answer3) == '111':
            cursor.execute(f'UPDATE lvl SET lvl = "2" WHERE user_id = "{message.chat.id}"')
            cursor.execute(f'UPDATE courses SET company = "Сдал" WHERE user_id = "{message.chat.id}"')
            conn.commit()
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_won,
                                  reply_markup=menu.menu_back_to_learning_menu)
        else:
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_defeat,
                                  reply_markup=menu.menu_back_to_learning_menu)
    

    def test_pizza_stage_1(message):
        if message.text == '1':
            answer1 = '1'
        else:
            answer1 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_pizzamaker_text_2)
        bot.register_next_step_handler(msg, test_pizza_stage_2, answer1)
    def test_pizza_stage_2(message, answer1):
        if message.text == '1':
            answer2 = '1'
        else:
            answer2 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_pizzamaker_text_3)
        bot.register_next_step_handler(msg, test_pizza_stage_3, answer1, answer2)
    def test_pizza_stage_3(message, answer1, answer2):
        if message.text == '1':
            answer3 = '0'
        else:
            answer3 = '1'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        if (answer1 + answer2 + answer3) == '111':
            cursor.execute(f'UPDATE courses SET pizzamaker = "Сдал" WHERE user_id = "{message.chat.id}"')
            conn.commit()
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_won,
                                  reply_markup=menu.menu_back_to_learning_menu)
        else:
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_defeat,
                                  reply_markup=menu.menu_back_to_learning_menu)
            

    def test_cassier_stage_1(message):
        if message.text == '1':
            answer1 = '1'
        else:
            answer1 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_cassier_text_2)
        bot.register_next_step_handler(msg, test_cassier_stage_2, answer1)
    def test_cassier_stage_2(message, answer1):
        if message.text == '1':
            answer2 = '1'
        else:
            answer2 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_cassier_text_3)
        bot.register_next_step_handler(msg, test_cassier_stage_3, answer1, answer2)
    def test_cassier_stage_3(message, answer1, answer2):
        if message.text == '1':
            answer3 = '0'
        else:
            answer3 = '1'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        if (answer1 + answer2 + answer3) == '111':
            cursor.execute(f'UPDATE courses SET cassier = "Сдал" WHERE user_id = "{message.chat.id}"')
            conn.commit()
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_won,
                                  reply_markup=menu.menu_back_to_learning_menu)
        else:
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_defeat,
                                  reply_markup=menu.menu_back_to_learning_menu)
    

    def test_manager_stage_1(message):
        if message.text == '1':
            answer1 = '1'
        else:
            answer1 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_manager_text_2)
        bot.register_next_step_handler(msg, test_manager_stage_2, answer1)
    def test_manager_stage_2(message, answer1):
        if message.text == '1':
            answer2 = '1'
        else:
            answer2 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_manager_text_3)
        bot.register_next_step_handler(msg, test_manager_stage_3, answer1, answer2)
    def test_manager_stage_3(message, answer1, answer2):
        if message.text == '1':
            answer3 = '0'
        else:
            answer3 = '1'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        if (answer1 + answer2 + answer3) == '111':
            cursor.execute(f'UPDATE courses SET manager = "Сдал" WHERE user_id = "{message.chat.id}"')
            conn.commit()
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_won,
                                  reply_markup=menu.menu_back_to_learning_menu)
        else:
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_defeat,
                                  reply_markup=menu.menu_back_to_learning_menu)
            
    

    def test_teacher_stage_1(message):
        if message.text == '1':
            answer1 = '1'
        else:
            answer1 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_teacher_text_2)
        bot.register_next_step_handler(msg, test_teacher_stage_2, answer1)
    def test_teacher_stage_2(message, answer1):
        if message.text == '1':
            answer2 = '1'
        else:
            answer2 = '0'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = bot.send_message(chat_id=message.chat.id,
                                  text=text.test_teacher_text_3)
        bot.register_next_step_handler(msg, test_teacher_stage_3, answer1, answer2)
    def test_teacher_stage_3(message, answer1, answer2):
        if message.text == '1':
            answer3 = '0'
        else:
            answer3 = '1'
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        if (answer1 + answer2 + answer3) == '111':
            cursor.execute(f'UPDATE courses SET teacher = "Сдал" WHERE user_id = "{message.chat.id}"')
            conn.commit()
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_won,
                                  reply_markup=menu.menu_back_to_learning_menu)
        else:
            bot.send_message(chat_id=message.chat.id,
                                  text=text.test_defeat,
                                  reply_markup=menu.menu_back_to_learning_menu)
            

    bot.polling(none_stop=True)

start_bot()