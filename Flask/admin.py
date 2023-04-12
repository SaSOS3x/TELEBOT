from flask import Flask,render_template,request
from hashlib import md5
import sqlite3
import telebot
import os

path = os.getcwd()
app = Flask(__name__)

os.chdir('..')
db = sqlite3.connect('base_pyramid.db',check_same_thread=False)
cursor = db.cursor()
os.chdir(path)
log = ''
access = False
@app.route('/')
def index():
    return render_template('auth.html',title='Authorization')

@app.route('/auth_token',methods=["POST"])
def auth_token():
    global log,access
    log = request.form['auth_login']
    passw = md5(request.form['auth_password'].encode('utf-8')).hexdigest()
    global cursor
    cursor.execute('SELECT login,pass FROM admin')
    for i in list(cursor.fetchall()):
        if (log,passw) == i:
            access = True
            return render_template('index.html', people=cursor.execute('SELECT user_id,login,data,access FROM users').fetchall()
                                   ,title='Admin panel', login = log)
                                   
        else:
            access = False
            return render_template('auth.html',title='Authorization')
        
@app.route('/declare')
def declare():
    global access
    if access == True:
        return render_template('declare.html', login=log,title='Declare')
    else:
        access = False  
        return render_template('auth.html',title='Authorization')
@app.route('/sendmessage', methods=['POST'])
def sendmessage():
    global cursor
    title=request.form['title_message']
    text=request.form['text_message']
    bot = telebot.TeleBot('5703032509:AAGbUu378C8wUa3RYbTLSO9LkeTFLAXZcW4')
    for i in cursor.execute('SELECT user_id FROM users'):
        bot.send_message(i[0], f'<b>{title}</b>\n{text}',parse_mode='HTML')
    return render_template('declare.html', login=log,title='Declare')
    


if __name__ == '__main__':
    app.run(debug=True)