import hashlib
import sqlite3

db = sqlite3.connect('base_pyramid.db',check_same_thread=False)
cursor = db.cursor()

login = input('login: ')
password =hashlib.md5(input('password: ').encode('utf-8')).hexdigest()

print(f'login: {login}\npassword: {password}')

cursor.execute('INSERT INTO admin VALUES (?,?)',[login,password])
db.commit()