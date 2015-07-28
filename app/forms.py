from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, RadioField,validators
 
class UserForm(Form):
  username = TextField("Username",[validators.Required()])
  password = TextField("Password",[validators.Required()])
  homefolder = TextField("HomeFolder",[validators.Required()])
  shelltype = TextField("ShellType",[validators.Required()])
  sudo_options = RadioField('Options', choices=[('yes','YES'),('no','NO')])
  submit = SubmitField("Submit")

class ModifyForm(Form):
  value1 = TextField("Value1")
  value2 = TextField("Value2")
  value3 = TextField("Value3")
  value4 = TextField("Value4")
  options = RadioField("Options1", choices=[('username','USERNAME'),('homedir','HOME DIR'),('password','PASSWORD')])
  submit1 = SubmitField("Submit1")
