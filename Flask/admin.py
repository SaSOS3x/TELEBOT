from flask import Flask,render_template,request
from hashlib import md5


app = Flask(__name__)




@app.route('/')
def index():
    return render_template('auth.html')

@app.route('/auth_token',methods=["POST"])
def auth_token():
    log = md5(request.form['auth_login'].encode('utf-8')).hexdigest()
    print(request.form['auth_password'])
    passw = md5(request.form['auth_password'].encode('utf-8')).hexdigest()
    with open('pass.txt','r+') as admin:
        rows = admin.readlines()
        for row in rows:
            row.split(' ')
            if md5(row[0].encode('utf-8')).hexdigest() == log and md5(row[1].encode('utf-8')).hexdigest() == passw:
                return render_template('index.html')
            else:
                return '<h1>WRONG PASSWORD or LOGIN</h1>'

if __name__ == '__main__':
    app.run(debug=True)