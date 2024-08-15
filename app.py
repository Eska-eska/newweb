from flask import Flask, render_template, request, jsonify
from db import connecter as mydb

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    balance = 33
    return render_template('home.html',balance = balance)

@app.route('/json', methods=["POST"])
def datares():
    
    data = request.get_json()
    val = data['value']
    w = data['what']
    
    username = "."
    
    query = "Select data From user Where username=%s"
    mycursor.execute(query, username)
    sqldata = mycursor.fetchall()

    if w == 'add':
        sqldata = sqldata + val
    else:
        sqldata = sqldata - val
    
    query ="""  UPDATE user
                SET data = %s
                WHERE username = %s;"
            """
    mycursor.execute(query,(sqldata,username))
    mydb.commit()

    return jsonify({})