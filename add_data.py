
import mysql.connector as mc
from mysql.connector import Error
from flask import request,jsonify


def add_emp_dt(data):   


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
            cursor.execute("""create table if not exists employee_data
            (Emp_id INT PRIMARY KEY AUTO_INCREMENT,
            First_name VARCHAR(255) NOT NULL,
            Last_name VARCHAR(255) NOT NULL,
            Department VARCHAR(255) NOT NULL,
            Department_Id varchar(255) NOT NUll,
            Salary Varchar(255) NOT NULL)""")

            data = request.get_json()

            First_name = data.get("first_name")
            Last_Name = data.get("last_name")
            Department = data.get("department")
            Department_Id = data.get("department_id")
            Salary = data.get("salary")
            

            if not First_name or not Last_Name or not Department or not Department_Id or not Salary:
                return jsonify({"Error":"All fields are required"})
            
            insert_data = """insert into employee_data (First_name,Last_name,Department,Department_Id,Salary)
            values (%s,%s,%s,%s,%s)"""
            data = (First_name,Last_Name,Department,Department_Id,Salary)
            cursor.execute(insert_data,data)
            db.commit()
            return jsonify({"Result":"User Data has been Added Succesfull..."})  

    except Error as er:
        return jsonify({"Database Connection":f"Error occured while connecting to database: str{(er)}"})

    # finally:
    #     if cursor:
    #         cursor.close()
    #     if db and db.is_connected:
    #         db.close()
    #         print("MySQL connection is closed")

    # return True

# while True:
#     if not add_emp_dt():
#         break

