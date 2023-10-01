import streamlit as sl
import mysql.connector as mysql
import os 


db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_database = os.environ.get("DB_DATABASE")


connection = mysql.connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db_database
)

cursor = connection.cursor()


sl.set_page_config(page_title='Amaan',layout='centered')
sl.title('College Database')

select_box = sl.selectbox('Select',('Staff','Student'))
if select_box == 'Student':
    stu_id = sl.text_input('Enter your Student ID :')
    stu_name = sl.text_input('Enter your Name:')
    stu_age = sl.text_input('Enter your Age:')
    stu_course = sl.selectbox('Select your Course',('science','maths'))
    stu_btn = sl.button('Submit',key='student')
    
    if stu_btn:
        sl.markdown(f'''
        ID ={stu_id}
        Name = {stu_name}
        Age = {stu_age}
        Course = {stu_course}'''
        )
        stu_insert = "insert into student (id,name,age,course) values (%s,%s,%s,%s)"
        cursor.execute(stu_insert,(stu_id,stu_name,stu_age,stu_course))
        cursor.execute('commit')

else :
    stf_id = sl.text_input('Enter your Staff ID:')
    stf_name = sl.text_input('Enter your Name:')
    stf_age = sl.text_input('Enter Your Age:')
    stf_dept = sl.text_input('Enter your department:')
    stf_btn = sl.button('Submit',key='staff')
    if stf_btn :
        sl.markdown(f'''
        ID ={stf_id}
        Name = {stf_name}
        Age = {stf_age}
        Course = {stf_dept}'''
        )
        stf_insert = "insert into staff (id,name,age,department) values(%s,%s,%s,%s)"
        cursor.execute(stf_insert,(stf_id,stf_name,stf_age,stf_dept))
        cursor.execute('commit')

