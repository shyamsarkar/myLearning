from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
		name = request.form['name']
		addr = request.form['add']
		city = request.form['city']
		pin = request.form['pin']

		with sql.connect("one.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO table1 (name,addr,city,pin) VALUES (?,?,?,?)",(name,addr,city,pin))
			con.commit()
	return render_template('student.html')

@app.route('/list')
def list():
	con = sql.connect("one.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from table1")
	rows = cur.fetchall()
	return render_template('result.html', rows=rows)

@app.route('/create', methods=['POST', 'GET'])
def create_db():
	if request.method=='POST':
		db = request.form['db']
		db=db+".db"
		conn = sqlite3.connect(db)
		print("Opened database successfully")
		conn.execute('CREATE TABLE table1 (name TEXT, addr TEXT, city TEXT, pin TEXT)')
		print("Table created successfully")
		conn.close()
	return redirect(url_for('home'))

app.run(debug=True)