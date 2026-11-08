import sys
sys.path.insert(0, 'db/')

from flask import Flask, render_template, request, redirect, url_for, session, flash 

from db.dbhelper import deleterecord, getall, getrecord, updatestudent,addstudent


app:any = Flask(__name__)
app.secret_key='febe9854-9ac3-40d2-ab41-49a973d61446'

@app.after_request
def after_request(response)->None:
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/')
def index()->None:
    if 'email' in session:
        return redirect(url_for('main'))
    return render_template('index.html')

@app.route("/main")
def main()->None:
    if 'email' in session:
        students:list = getall("students")
        return render_template("main.html",slist=students)
    else:
        return redirect(url_for('index'))

@app.route("/userlogin",methods=['POST'])
def userlogin()->None:
    email:str = request.form['email']
    password:str = request.form['password']
    user:list = getrecord('users',email=email,password=password)

    if len(user)>0:
        session['email'] = email
        flash("Login Successful")
        return redirect(url_for('main'))
    else:
        flash("Login Failed! Credentials do not match.")
        return redirect(url_for('index'))

@app.route("/addstudent", methods=['POST'])
def add_student():
    if 'email' not in session:
        return redirect(url_for('index'))
    
    idno = request.form['idno']
    lastname = request.form['lastname']
    firstname = request.form['firstname']
    course = request.form['course']
    level = request.form['level']

    if addstudent(idno=idno, lastname=lastname, firstname=firstname, course=course, level=level):
        flash("Student added successfully!")
    else:
        flash("Failed to add student. ID No may already exist.")
    return redirect(url_for('main'))

@app.route("/updatestudent", methods=['POST'])
def update_student():
    if 'email' not in session:
        return redirect(url_for('index'))

    idno = request.form['idno']
    lastname = request.form['lastname']
    firstname = request.form['firstname']
    course = request.form['course']
    level = request.form['level']

    if updatestudent(idno, lastname=lastname, firstname=firstname, course=course, level=level):
        flash("Student updated successfully!")
    else:
        flash("Failed to update student.")
    return redirect(url_for('main'))

@app.route("/deletestudent/<idno>")
def delete_student(idno):
    if 'email' not in session:
        return redirect(url_for('index'))

    if deleterecord("students", idno=idno):
        flash("Student deleted successfully!")
    else:
        flash("Failed to delete student.")
    return redirect(url_for('main'))



@app.route("/logout")
def logout()->None:
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)