from flask import Flask, render_template, request, flash
from forms import UserForm, ModifyForm
import os, pwd, crypt

app = Flask(__name__)
app.secret_key = 'feifnsdlfnas32423'

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/create', methods=['GET', 'POST'])
def create():
  form = UserForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('user.html', form=form)
    elif form.username.data in [x[0] for x in pwd.getpwall()]:
        flash('User Exists')
        return render_template('user.html', form=form)
    elif os.path.isabs(form.homefolder.data) == False:
        flash('Enter valid home dir')
        return render_template('user.html', form=form)
    elif os.path.exists(form.shelltype.data) == True  and open('/etc/shells','r').read().find(form.shelltype.data) > 0:
        os.system("useradd -md "+ form.homefolder.data +" -s " + form.shelltype.data +" -p "+ form.password.data +"  "+ form.username.data)
        flash('User Added Successfully')
        return render_template('user.html', form=form)
    else:
	flash ('Enter valid shell type')
	return render_template('user.html', form=form)
  elif request.method == 'GET':
    return render_template('user.html', form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
  form = UserForm()
  if request.method == 'POST':
    if form.username.data in [x[0] for x in pwd.getpwall()]:
	os.system("userdel " +form.username.data)
	flash('User Delete successfully')
	return render_template('user_del.html', form=form)
    else:
        flash('Enter valid User')
        return render_template('user_del.html', form=form)
  elif request.method == 'GET':
	return render_template('user_del.html', form=form)

@app.route('/modify', methods=['GET', 'POST'])
def modify():
  form = ModifyForm()

  if request.method == 'POST':
    if form.options.data =='username':
      if form.value1.data  in [x[0] for x in pwd.getpwall()] and form.value1.data == True and form.value2.data != None:
        os.system("usermod -l "+ form.value2.data +" " + form.value1.data )
        flash('Username modified')
        return render_template('modify.html', form=form)
      else:
        flash('enter valid old and new username')
        return render_template('modify.html', form=form)
    elif form.options.data == 'password':
      if form.value1.data  in [x[0] for x in pwd.getpwall()] and form.value4.data == True:
        os.system("usermod -p " + form.value4.data +" " + form.value1.data)
        flash("password updated")
        return render_template('modify.html', form=form)
      else:
        flash('enter valid username and password')
        return render_template('modify.html', form=form)
    elif form.options.data == 'homedir':
      if form.value1.data  in [x[0] for x in pwd.getpwall()] and  os.path.isabs(form.value3.data) == True:
        os.system("usermod -d " + form.value3.data +" " + form.value1.data)
        flash("home dir updated")
        return render_template('modify.html', form=form)
      else:
        flash('enter valid username and home dir')
        return render_template('modify.html', form=form)
    else:
      flash('select an option')
      return render_template('modify.html', form=form)

  elif request.method == 'GET':
    return render_template('modify.html', form=form)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

