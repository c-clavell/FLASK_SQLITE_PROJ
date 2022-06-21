from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddSomethingForm(FlaskForm):
    name=StringField('Name', validators=[DataRequired()]) 
    email=StringField('email', validators=[DataRequired()]) 

    submit=SubmitField('Submit')
    generate=SubmitField('Generate')
    send=SubmitField('Send')

class DeleteForm(FlaskForm):
    id=StringField('ID', validators=[DataRequired()]) 
    delete=SubmitField('Delete')


class EditForm(FlaskForm):
    id_edit=StringField('ID_edit',validators=[DataRequired()])
    edit=SubmitField('Edit')

    name_edit=StringField('Name_edit',validators=[])
    email_edit=StringField('EMAIL_edit',validators=[])

    accept=SubmitField('Accept')
    cancel=SubmitField('Cancel')


    


# class EditForm(FlaskForm):
#     id_edit=StringField('ID_edit',validators=[DataRequired()])
#     edit_edit=SubmitField('Edit_edit')

#     name_edit=StringField('Name_edit',validators=[DataRequired()])
#     email_edit=StringField('EMAIL_edit',validators=[DataRequired()])

#     accept=SubmitField('Accept')
#     cancel=SubmitField('Cancel')

