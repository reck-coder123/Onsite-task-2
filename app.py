from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
 
 
app.secret_key = 'rohit23'
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pikachu2022#$'
app.config['MYSQL_DB'] = 'hirelogin'
 
 
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html");

@app.route('/LoginA', methods=['GET', 'POST'])
def LoginA():
    msg = ''
    if request.method == 'POST' and 'usernameA' in request.form and 'passwordA' in request.form:
        usernameA = request.form['usernameA']
        passwordA = request.form['passwordA']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM Job WHERE usernameA = % s AND passwordA = % s', (usernameA, passwordA, ))
        Account = cursor.fetchone()
        if Account:
            session['loggedin'] = True
            session['id'] = Account['id']
            session['usernameA'] = Account['usernameA']
            msg = 'Logged in successfully !'
            return render_template('indexA.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('loginA.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('usernameA', None)
    return redirect(url_for('home'))

@app.route('/registerA',methods=['GET', 'POST'])
def registerA():
    msg=''
    if request.method == 'POST' and 'nameA' in request.form and 'usernameA' in request.form and 'emailA' in request.form and 'passwordA' in request.form:
        nameA=request.form['nameA']
        usernameA=request.form['usernameA']
        emailA=request.form['emailA']
        passwordA=request.form['passwordA']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM Job WHERE nameA = % s and usernameA= %s', (nameA, usernameA))
        Account = cursor.fetchone()
        if Account:
            msg='Account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', emailA):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z]+', nameA):
            msg = 'Enter your Name properly'
        elif not re.match(r'[A-Za-z0-9]+', usernameA):
            msg = 'Username must contain only characters and numbers !'
        elif not nameA or not usernameA or not passwordA or not emailA  :
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO Job VALUES (NULL,%s, % s, % s, % s)',
                           (nameA, usernameA, passwordA, emailA))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    return render_template("registerA.html",msg=msg)

@app.route('/LoginJ', methods=['GET', 'POST'])
def LoginJ():
    msg = ''
    if request.method == 'POST' and 'usernameJ' in request.form and 'passwordJ' in request.form:
        usernameJ = request.form['usernameJ']
        passwordJ = request.form['passwordJ']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM New WHERE usernameJ = % s AND passwordJ = % s', (usernameJ, passwordJ, ))
        Account = cursor.fetchone()
        if Account:
            session['loggedin'] = True
            session['id'] = Account['id']
            session['usernameJ'] = Account['usernameJ']
            msg = 'Logged in successfully !'
            return render_template('indexJ.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('loginJ.html', msg=msg)

@app.route('/registerJ',methods=['GET', 'POST'])
def registerJ():
    msg=''
    if request.method == 'POST' and 'nameJ' in request.form and 'usernameJ' in request.form and 'emailJ' in request.form and 'passwordJ' in request.form:
        nameJ=request.form['nameJ']
        usernameJ=request.form['usernameJ']
        emailJ=request.form['emailJ']
        passwordJ=request.form['passwordJ']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM New WHERE nameJ = % s and usernameJ= %s', (nameJ, usernameJ))
        Account = cursor.fetchone()
        if Account:
            msg='Account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', emailJ):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z]+', nameJ):
            msg = 'Enter your Name properly'
        elif not re.match(r'[A-Za-z0-9]+', usernameJ):
            msg = 'Username must contain only characters and numbers !'
        elif not nameJ or not usernameJ or not passwordJ or not emailJ  :
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO New VALUES (NULL,%s, % s, % s, % s)',
                           (nameJ, usernameJ, passwordJ, emailJ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    return render_template("registerJ.html",msg=msg)

@app.route('/indexA')
def indexA():
    if 'loggedin' in session:
        return render_template("indexA.html")
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
        if request.method=='POST' and 'job' in request.form and 'description' in request.form:
            job=request.form['job']
            description=request.form['description']
            cursor=mysql.connection.cursor()
            cursor.execute('INSERT INTO info VALUES(NULL,%s,%s)',(job,description,))
            mysql.connection.commit()
            msg='Job profile added successfully'
        return render_template("add_job.html",msg=msg)
    return redirect(url_for('LoginA'))

@app.route("/display_job")
def display_job():
    if 'loggedin' in session:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM info ')
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
            cursor.execute('INSERT INTO choose VALUES(NULL,%s,%s)',(Name,jprofile,))
            mysql.connection.commit()
            msg='You have successfully applied'
        return render_template("view.html",msg=msg)
    return redirect(url_for('LoginJ'))

@app.route("/show_application")
def show_application():
    if 'loggedin' in session:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM choose ')
        applicants=cursor.fetchall()
        return render_template("applicant.html",applicants=applicants)
    return redirect(url_for('LoginA'))



if __name__ == '__main__':
    app.run(debug=True)