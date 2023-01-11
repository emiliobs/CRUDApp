from flask import Flask, flash, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

# index methos


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', students=data)

# Insert Method


@app.route('/insert',  methods=['POST'])
def insert():
	if request.method == "POST":

		flash("Data Inserted Successfully!")

		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']

		cur = mysql.connection.cursor()
		cur.execute("Insert Into students (name, email, phone) Values (%s, %s, %s)", (name, email, phone))
		mysql.connection.commit()

		return redirect(url_for('Index'))

if __name__ == "__main__":
	app.run(port=5555, debug=True)
