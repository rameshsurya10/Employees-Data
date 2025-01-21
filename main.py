from Register import regi
from login import log,for_pass,for_un
from add_data import add_emp_dt
from emp_data import emp_dt
from alter_data import update,delete
from flask import Flask,request,jsonify



    
# def main():
#     while True:
#         print("\n1. REGISTER")
#         print("2. LOG IN")
#         print("3. ADD DATA")
#         print("4. VIEW DATA")
#         print("5. ALTER_DATA")
#         print("6. Exit")

#         choice = input('Enter the choice : ')
        
#         if choice == "1":
#             Register.regi()
#             break
#         elif choice == "2":
#             login.log()
#             break
#         elif choice == "3":
#             add_data.add_emp_dt()
#             break
#         elif choice == "4":
#             emp_data.emp_dt()
#             break
#         elif choice == "5":
#             alter_data.alter()
#             break
#         elif choice == "6":
#             print("Exit from DATABASE...")
#             break
#         else:
#             print("Enter the valid option!!!")
# main()


app = Flask(__name__)

# For registration 

@app.route("/register", methods=["POST"])

def register():

    data = request.get_json()

    return regi(data) 

# For login 

@app.route("/login",methods = ["POST"])

def login():
    data = request.get_json()

    return log(data)

# For Update Password

@app.route("/login/change_password",methods = ["POST"])

def fr_ps():
    data = request.get_json()

    return for_pass(data)

#For Update Username

@app.route("/login/change_username",methods = ["POST"])

def fr_un():
    data = request.get_json()

    return for_un(data)

# For Add employees Data

@app.route("/add_employee_data",methods = ["POST"])

def Add_Emp_data():
    data = request.get_json()

    return add_emp_dt(data)

# For Employee Data

@app.route("/employee_data",methods = ["POST"])

def employee_data():
    data = request.get_json()

    return emp_dt(data)

# For Update Data

@app.route("/alter/update",methods = ["POST"])

def update_data():
    data = request.get_json()

    return update(data)

# For Delete Data

@app.route("/alter/delete",methods = ["POST"])

def delete_data():
    data = request.get_json()

    return delete(data)




if __name__=="__main__":
    app.run(debug=True)

    