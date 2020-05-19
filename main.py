from flask import Flask,render_template,request,redirect,flash,session
from flask_mysqldb import MySQL

app=Flask(__name__,template_folder='templates')
app.secret_key='many rndom bytes'

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="bush"
app.config['MYSQL_PASSWORD']="bush"
app.config['MYSQL_DB']="contact"
mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("select * from users where username=%s", (username,))
        data = cur.fetchall()
        if data:
            flash('username/password Already exist')
            return redirect('/')
        else:
            cur.execute("INSERT INTO users(username,email,password) VALUES(%s,%s ,%s)", (username, email, password))
            mysql.connection.commit()
            flash('successfull registred')
            return redirect('/login')
    else:
        return render_template('register.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password=request.form['password']
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password,))
        data=cur.fetchone()
        mysql.connection.commit()
        if data:
            return redirect('/index')
        else:
            flash('invalid uername password')
            return render_template('login.html')

    else:
          return render_template('/login.html')
@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM add_new")
    data = cur.fetchall()
    cur.close()
    return render_template('home.html', info=data )
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect('/login')
@app.route('/add_new',methods=['GET','POST'])
def add_new():
    if request.method=='POST':
        flash('data added succesfully..!!')
        phone_no1=request.form.get('phone_no1')
        name=request.form.get('name')
        email=request.form.get('email')
        phone_no2 = request.form.get('phone_no2')
        company=request.form.get('company')
        group_name=request.form.get('group')
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO add_new(phone_no1,name,email,phone_no2,company,group_name) VALUES(%s,%s,%s ,%s,%s,%s)",(phone_no1,name,email,phone_no2,company,group_name))
        mysql.connection.commit()
        data=cur.fetchall()
        return redirect('/home')
    else:
        group=['family','friends','relatives','collegues']
        return render_template('add_new.html',data=group)


@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
     flash("Record Has Been Deleted Successfully")
     cur=mysql.connection.cursor()
     cur.execute("""DELETE FROM add_new WHERE id=%s""",(id,))
     mysql.connection.commit()
     return redirect('/home')
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM add_new WHERE id=%s",(id,))
    data=cur.fetchall()
    if request.method=='POST':
        phone_no1=request.form['phone_no1']
        name=request.form['name']
        email=request.form['email']
        phone_no2 = request.form['phone_no2']
        company=request.form['company']
        group_name = request.form.get('group')
        cur=mysql.connection.cursor()
        cur.execute('''UPDATE add_new SET phone_no1=%s , name=%s, email=%s ,phone_no2=%s ,company=%s ,group_name=%s WHERE id=%s''',(phone_no1,name,email,phone_no2,company,group_name,id))
        mysql.connection.commit()
        flash("Data Updated Successfully....")
        return redirect('/home')
    else:
        grp=['','family','friends','relatives','collegues']
        return render_template('edit.html',data=data, serial=id,grp=grp)

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':
        tag=request.form['search']
        search="%{0}%".format(tag)
        cur=mysql.connection.cursor()
        cur.execute("select * from add_new WHERE name LIKE '{0}'".format(search))
        data=cur.fetchall()
        if data:
            return render_template('home.html',info=data)
        else:
            flash('No Contact Found!!')
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
