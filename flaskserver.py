
from flask import Flask

app = Flask(__name__) 

from flask import render_template
from flask import Flask, render_template 
from flask import url_for 
from flask import request 
from flask import redirect, abort  
import csv 

@app.route("/urlfor") 
def urlfor():
    print(url_for('static', filename='favicon.ico')) 
    return url_for('static', filename='favicon.ico') 

@app.route("/") 
@app.route("/index.html") 
def univ_home():
    return render_template("index.html")

@app.route("/<page_name>")  
def univ_page(page_name = ""): 
    return render_template(f"{page_name}") if page_name else render_template("index.html") 

def write_to_csv(data): 
    with open("database.csv", mode="a", newline="") as csv_database: 
        email = data["email"] #string
        subject = data["subject"] #string
        message = data["message"] #string
        print(email,subject,data)
        
        csv_writer = csv.writer(csv_database, delimiter=",", quoting=csv.QUOTE_NONNUMERIC) 
        csv_fieldheaders = ["email","subject","message"] 
        csv_rowfieldvalues = [email,subject,message]
        
        csv_writer.writerow(csv_rowfieldvalues) 

@app.route('/submit_form', methods=['POST', 'GET'])
def univ_submit_form(): 
    if request.method == "POST":
        data = request.form.to_dict() 
        write_to_csv(data)  
        return render_template("/thankyou.html", user_name=data["email"]) 

