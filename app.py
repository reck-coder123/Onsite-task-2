from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
 
 
app.secret_key = 'rohit23'
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pikachu2022#$'
app.config['MYSQL_DB'] = 'hiretlogin'
 
 
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html");

@app.route('/LoginA', methods=['GET', 'POST'])
def LoginA():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'passwordA' in request.form:
        username = request.form['username']
        passwordA = request.form['passwordA']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM Jobs WHERE username = % s AND passwordA = % s', (username, passwordA, ))
        Account = cursor.fetchone()
        if Account:
            session['loggedin'] = True
            session['id'] = Account['id']
            session['username'] = Account['username']
            msg = 'Logged in successfully !'
            return render_template('indexA.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('loginA.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/registerA',methods=['GET', 'POST'])
def registerA():
    msg=''
    if request.method == 'POST' and 'nameA' in request.form and 'username' in request.form and 'emailA' in request.form and 'passwordA' in request.form:
        nameA=request.form['nameA']
        username=request.form['username']
        emailA=request.form['emailA']
        passwordA=request.form['passwordA']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM Jobs WHERE nameA = % s and username= %s', (nameA, username))
        Account = cursor.fetchone()
        if Account:
            msg='Account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', emailA):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z]+', nameA):
            msg = 'Enter your Name properly'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not nameA or not username or not passwordA or not emailA  :
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO Jobs VALUES (NULL,%s, % s, % s, % s)',
                           (nameA, username, passwordA, emailA))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    return render_template("registerA.html",msg=msg)

@app.route('/LoginJ', methods=['GET', 'POST'])
def LoginJ():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'passwordJ' in request.form:
        username = request.form['username']
        passwordJ = request.form['passwordJ']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM News WHERE username = % s AND passwordJ = % s', (username, passwordJ, ))
        Account = cursor.fetchone()
        if Account:
            session['loggedin'] = True
            session['id'] = Account['id']
            session['username'] = Account['username']
            msg = 'Logged in successfully !'
            return render_template('indexJ.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('loginJ.html', msg=msg)

@app.route('/registerJ',methods=['GET', 'POST'])
def registerJ():
    msg=''
    if request.method == 'POST' and 'nameJ' in request.form and 'username' in request.form and 'emailJ' in request.form and 'passwordJ' in request.form:
        nameJ=request.form['nameJ']
        username=request.form['username']
        emailJ=request.form['emailJ']
        passwordJ=request.form['passwordJ']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM News WHERE nameJ = % s and username= %s', (nameJ, username))
        Account = cursor.fetchone()
        if Account:
            msg='Account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', emailJ):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z]+', nameJ):
            msg = 'Enter your Name properly'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not nameJ or not username or not passwordJ or not emailJ  :
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO News VALUES (NULL,%s, % s, % s, % s)',
                           (nameJ, username, passwordJ, emailJ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    return render_template("registerJ.html",msg=msg)

@app.route('/indexA')
def indexA():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT username FROM Jobs ')
        Admin = cursor.fetchone()
        if session['username']==Admin['username']:
            return render_template("indexA.html")
        return redirect(url_for('LoginA'))
    return redirect(url_for('home'))

@app.route('/indexJ')
def indexJ():
    if 'loggedin' in session:
        return render_template("indexJ.html")
    return redirect(url_for('home'))

@app.route('/add_jobs',methods=['GET','POST'])
def add_jobs():
    msg=''
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT username FROM Jobs ')
        Admin = cursor.fetchone()
        if session['username']==Admin['username'] :
            if request.method=='POST' and 'job' in request.form and 'description' in request.form:
                job=request.form['job']
                description=request.form['description']
                cursor=mysql.connection.cursor()
                cursor.execute('INSERT INTO infos VALUES(NULL,%s,%s)',(job,description,))
                mysql.connection.commit()
                msg='Job profile added successfully'
            return render_template("add_job.html",msg=msg)
        return redirect(url_for('LoginA'))
    return redirect(url_for('LoginA'))

@app.route("/display_job")
def display_job():
    if 'loggedin' in session:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM infos ')
        profile=cursor.fetchall()
        return render_template("view.html",profile=profile)
    return redirect(url_for('home'))

@app.route("/select",methods=['GET','POST'])
def select():
    msg=''
    if 'loggedin' in session:
        if request.method=='POST' and 'Name' in request.form and 'jprofile' in request.form :
            Name=request.form['Name']
            jprofile=request.form['jprofile']
            cursor=mysql.connection.cursor()
            cursor.execute('INSERT INTO chose VALUES(NULL,%s,%s)',(Name,jprofile,))
            mysql.connection.commit()
            msg='You have successfully applied'
        return render_template("view.html",msg=msg)
    return redirect(url_for('LoginJ'))

@app.route("/show_application")
def show_application():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT username FROM Jobs ')
        Admin = cursor.fetchone()
        if session['username']==Admin['username']:
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT * FROM chose ')
            applicants=cursor.fetchall()
            return render_template("applicant.html",applicants=applicants)
        return(redirect(url_for('LoginA')))
    return redirect(url_for('LoginA'))



if __name__ == '__main__':
    app.run(debug=True,port=int(8000))
