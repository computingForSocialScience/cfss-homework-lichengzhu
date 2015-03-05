from flask import Flask 
from flask import render_template
import pymysql # import MySQLdb

app = Flask(__name__)

conn = pymysql.connect(host='mcmahan.zapto.org',user='cfss15',passwd='computers',port=9999,db='cfss',charset='utf8')

cur = conn.cursor()

@app.route('/')
def country_index():
	sql = "SELECT name_en FROM countries"
	cur.execute(sql)
	names = []
	for name in cur.fetchall():
		names.append(name[0])
	return render_template('country_index.html', names_list=names)

@app.route('/hello')
@app.route('/hello/<inputname>')

def hello(inputname=None):     #each time I define a new arguments in the app.route, I need to define it here
    #return 'Hello World!'
    return render_template('hello.html', name = inputname)

if __name__ == '__main__':
	app.debug = True
	app.run(port=5002)
