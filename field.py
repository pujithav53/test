from flask_wtf import Form
from wtforms import TextField,SubmitField,IntegerField,TextAreaField,PasswordField,SelectField, RadioField

from wtforms import validators, ValidationError
class field(Form):
   SurveyonName = TextField("Name",[validators.Required("Please enter name.")])
   SurveyforName=TextField("Email id",[validators.Required("please enter email id.")])
   SurveytimeperiodName=PasswordField("Password",[validators.Required("enter password.")])
   SurveynumberName=PasswordField("conform password",[validators.Required("conform password.")])
   SurveynumberrName=IntegerField("Enter mobile number",[validators.Required("enter mobile number.")])
  
   
   submit = SubmitField("submit")





class login(Form):
   SurveyonName = TextField("Username",[validators.Required("Please enter username.")])
   SurveyforName=PasswordField("Password",[validators.Required("please enter password.")])
   submit = SubmitField("submit")



class createsurvey(Form):
   SurveyonName = TextField("Product Name",[validators.Required("Select the product.")])
   SurveyforName= SelectField("choose your topic",choices=[('ma','masakali'),('an','anarkali')])
   SurveytimeperiodName=IntegerField("Time period",[validators.Required("select time.")])
   
   submit = SubmitField("submit")


class publishsurvey(Form):
   usercount= IntegerField("Users Count",[validators.Required("enter numbr of users.")])
   Gender = RadioField('Gender', choices=[('M','Male'),('F','Female')]) 
   location = SelectField("Select the location",choices=[('ku', 'kukatpally'),('am','ameerpet'),('hi', 'hitechcity')])
   recursive = SelectField("Select time period ",choices=[('we', 'weekely'),('mn','monthly'),('ye', 'yearly')])
   
   submit = SubmitField("submit")


class viewusers(Form):
    website = IntegerField("Number of users through Website",[validators.Required("Enter number of users.")])
    mobile = IntegerField("Number of users through Mobile",[validators.Required("Enter number of users.")])
    submit = SubmitField("submit")




class viewusers(Form):
    website = IntegerField("Number of users through Website",[validators.Required("Enter number of users.")])
    mobile = IntegerField("Number of users through Mobile",[validators.Required("Enter number of users.")])
    submit = SubmitField("submit")
