from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, RadioField,validators
 
class UserForm(Form):
  username = StringField("Username",[validators.DataRequired()])
  password = StringField("Password",[validators.DataRequired()])
  homefolder = StringField("HomeFolder",[validators.DataRequired()])
  shelltype = StringField("ShellType",[validators.DataRequired()])
  submit = SubmitField("Submit")

class ModifyForm(Form):
  value1 = StringField("Value1")
  value2 = StringField("Value2")
  value3 = StringField("Value3")
  value4 = StringField("Value4")
  options = RadioField("Options1", choices=[('username','USERNAME'),('homedir','HOME DIR'),('password','PASSWORD')])
  submit1 = SubmitField("Submit1")

class SudoForm(Form):
  username = StringField("Username",[validators.DataRequired()])
  sudo_options = RadioField('Options', choices=[('yes','YES'),('no','NO')])
  submit = SubmitField("Submit")

