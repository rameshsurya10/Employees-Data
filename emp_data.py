
import mysql.connector as mc
from mysql.connector import Error
from flask import request,jsonify

def emp_dt(data):   


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

            cursor = db.cursor()

            data = request.get_json()

            firstname = data.get("First_name")
            lastname = data.get("Last_name")
            department = data.get("Depart")
            departid = data.get("Depart_id")
            salary = data.get("Salary")
            query = data.get("query")

            if query:
                    if query.strip() !="":
                        try:
                           cursor.execute(query)
                           results = cursor.fetchall()
                           return jsonify(results)
                        except Error as er:
                           return jsonify({"Query Error": "Please check the query you entered..."}), 400
                    else:
                        return jsonify({"Invalid Error": "Please enter the query to execute..."}), 400
                    
            query_bs = "select * from employee_data where 1=1"
            query_pa = []


            if firstname:
                    query_bs += "and First_name = %s"
                    query_pa.append(firstname)

            if lastname:
                    query_bs += "and Last_name = %s"
                    query_pa.append(lastname)

            if department:
                    query_bs += "and Department = %s"
                    query_pa.append(department)

            if departid:
                    query_bs += "and Department_id = %s"
                    query_pa.append(departid)

            if salary:
                    query_bs += "and Salary = %s"
                    query_pa.append(salary)

            
            cursor.execute(query_bs,tuple(query_pa))
            result = cursor.fetchall()

            return jsonify(result)
            
    except Error as er:
        return jsonify({"Database Connection ":"Error occured while connecting to database:{str(er)}"})
    # finally:
    #     if cursor:
    #         cursor.close()
    #     if db and db.is_connected:
    #         db.close()
    #         print("MySQL connection is closed")

    # return True

# while True:
#     if not emp_dt():
#         break
