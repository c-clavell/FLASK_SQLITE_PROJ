from flask import Flask, render_template as rt, request, url_for, flash, get_flashed_messages
from app import app
from faker import Faker
from datetime import datetime
from sql_tables import users_info_table

from app import db

fk=Faker()

import forms



@app.route('/')
def index():
    name="yoyo"
    return rt('simple.html', name=name)


@app.route('/input', methods=['GET','POST'])
def input():
    form=forms.AddSomethingForm()
    values = users_info_table.query.all()

    formDelete=forms.DeleteForm()
    formEdit=forms.EditForm()

    ## getting all ids in the table
    ids=users_info_table.query.with_entities(users_info_table.id).all()
    id_list=[i[0] for i in ids]

    
    ###############################################
    #edit
    if formEdit.validate_on_submit():
        idd=formEdit.id_edit.data

        
        if ('edit' in request.form) :

            if (int(idd) in id_list):
                info=users_info_table.query.filter_by(id=formEdit.id_edit.data).first()
                
                ## 
                formEdit.name_edit.data=info.name
                formEdit.email_edit.data=info.email
                
                return rt('input.html', form=form, values=values, formDelete=formDelete, formEdit=formEdit, info=info, flag=True )

            else:
                flash(f"ID: {idd} not found")
                return rt('input.html', form=form, values=values, formDelete=formDelete, formEdit=formEdit, flag=False )

        if 'cancel' in request.form:
            return rt('input.html', form=form, values=values, formDelete=formDelete, formEdit=formEdit, flag=False )

        if 'accept' in request.form:
            
            nn=formEdit.name_edit.data
            ee=formEdit.email_edit.data
            dt2=datetime.utcnow()

            new= users_info_table.query.filter_by(id=idd).first()
            new.name=nn
            new.email=ee
            new.date=dt2
            db.session.commit()

            flash(f'Entry with ID: {idd} modified')
            return rt('input.html', form=form, values=values, formDelete=formDelete, formEdit=formEdit, flag=False )

            


        
   


    #delete entries from table
    if formDelete.validate_on_submit():

        idDelete=formDelete.id.data
        idx=users_info_table.query.filter_by(id=idDelete).first()

        ##checking if id exists
        try:
            idx.id
        except:
            flash(f'ID {idDelete} does not exists')
            
        else:
            users_info_table.query.filter_by(id=idDelete).delete()
            db.session.commit()
            flash(f'Entry {idDelete} removed')

        finally:
            values = users_info_table.query.all()
            form.name.data='sample'
            form.email.data='sample@sample.com'
            return rt('input.html', form=form, values=values, formDelete=formDelete,formEdit=formEdit )

        

    
    ## get values form the form name and email
    if form.validate_on_submit():

        if 'generate' in request.form:
            form.name.data=fk.name()
            form.email.data=fk.email()
            return rt('input.html', form=form, values=values, formDelete=formDelete,formEdit=formEdit )

        if 'submit' in request.form:
            n=form.name.data
            e=form.email.data
            dt2=datetime.utcnow()
            entry=users_info_table(name=n, email=e, date=dt2)

            db.session.add(entry)
            db.session.commit()
            values = users_info_table.query.all()

            form.name.data='sample'
            form.email.data='sample@sample.com'

            return rt('input.html',form=form, values= values, n=n,e=e,dt=dt2, formDelete=formDelete,formEdit=formEdit)
        # return rt('input.html', form=form, n=n, e=e)


    ## adding default values
    form.name.data='sample'
    form.email.data='sample@sample.com'
    
    return rt('input.html', form=form,values=values,formDelete=formDelete,formEdit=formEdit)
