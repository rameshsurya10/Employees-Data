import mysql.connector as mc
from mysql.connector import Error
from flask import Flask, request, jsonify

app = Flask(__name__)


User_name = "Admin"
Password = "Admin@123"


def update(data):

    try:
        db = mc.connect(
            host = "localhost",
            database = "employees",
            user = "root",
            password = "Rameshsurya@08"
        )

        data = request.get_json()

        connection = None
        cursor = None

        cursor = db.cursor()

        user_name = data.get("username")
        password = data.get("password")
        
        if user_name == User_name and password == Password:

            first_name = data.get("firstname")
            last_name = data.get("lastname")
            department = data.get("department")
            department_id = data.get("department_id")
            salary = data.get("salary")

            query = "Update employee_data set "

            result=[]

            if first_name != '':
                query += "First_name = %s"
                result.append(first_name)
            
            if last_name != '':
                query += "Last_name = %s"
                result.append(last_name)

            if department != '':
                query += "Department = %s"
                result.append(department)

            if department_id != '':
                query += "Department_id = %s"
                result.append(department_id)

            if salary != '':
                query += "Salary = %s"
                result.append(salary)

            query += "where Emp_id = %s"
            
            result.append(data.get("emp_id"))

            query = query.rstrip(" ,")            
            
            cursor.execute(query,tuple(result))
            cursor.fetchall()

            db.commit()

            return jsonify({"Result":"Updated Successfull"})
        
        else:
            return jsonify({"Error":"Admin only have the access to update tha data"})
        

            
    except Error as er:
        return jsonify({"Database Connection":f"Error occured while connecting to database: str{(er)}"})
    

def delete(data):

    try:
        db = mc.connect(
            host = "localhost",
            database = "employees",
            user = "root",
            password = "Rameshsurya@08"
        )

        data = request.get_json()

        connection = None
        cursor = None

        cursor = db.cursor()

        user_name = data.get("username")
        password = data.get("password")
        
        if user_name == User_name and password == Password:

            query = "delete from employee_data where Emp_id = %s"
            emp_no = data.get("emp_id")

            cursor.execute(query,tuple(emp_no))

            cursor.fetchall()

            db.commit()

            return jsonify({"Result":"Data has been deleted..."})
        else:
            return jsonify({"Error":"Admin only have the access to delete the data..."})
        
    except Error as er:
        return jsonify({"Error":f"Error occured while connecting to the database,str{(er)}"})
    

