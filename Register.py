import mysql.connector as mc
from mysql.connector import Error
from flask import request, jsonify


def regi(data):   

    connection = None
    cursor = None

    try:
        db = mc.connect(
            host = "localhost",
            database = "employees",
            user = "root",
            password = "Rameshsurya@08"
        )

        if db.is_connected:
            print("Databse is connected...")

            cursor = db.cursor()
            cursor.execute("""create table if not exists employees_users
            (id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password varchar(255) NOT NUll)""")

            print("employees_Users table is Active...")

            data = request.get_json()
            

            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not email or not password :
                if len(password) < 8:
                    return jsonify({"Error" : "Password Should be more then 8 letters/numbers/symbols/special Characters"}) 
                return jsonify({"Error":'All Fields are Required!!!'})

            
            insert_data = """insert into employees_users (username,email,password)values (%s,%s,%s)"""
            data = (username,email,password)
            cursor.execute(insert_data,data)
            db.commit()
            return jsonify({'Result' : "User Data has been Added Succesfull..."})

    except Error as er:
        return jsonify({"Error occured while connecting to database",er})

    # finally:
    #     if cursor:
    #         cursor.close()
    #     if db and db.is_connected:
    #         db.close()
    #         print("MySQL connection is closed")

    # return True

# while True:
#     if not regi():
#         break
