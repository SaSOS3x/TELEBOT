from flask import Flask,render_template,request
from hashlib import md5
import sqlite3
import os

path = os.getcwd()
app = Flask(__name__)

os.chdir('..')
db = sqlite3.connect('base_pyramid.db',check_same_thread=False)
cursor = db.cursor()
os.chdir(path)

@app.route('/')
def index():
    return render_template('auth.html')

@app.route('/auth_token',methods=["POST"])
def auth_token():
    log = request.form['auth_login']
    passw = md5(request.form['auth_password'].encode('utf-8')).hexdigest()
    global cursor
    cursor.execute('SELECT login,pass FROM admin')
    for i in list(cursor.fetchall()):
        if (log,passw) == i:
            
            return render_template('index.html', people=cursor.execute('SELECT user_id,login,data,access FROM users').fetchall()
                                   ,title='Admin panel', login = log)
        else:
            return render_template('auth.html')

if __name__ == '__main__':
    app.run(debug=True)