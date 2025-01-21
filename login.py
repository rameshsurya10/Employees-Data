import mysql.connector as mc
from mysql.connector import Error
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    """Helper function to establish and return a database connection."""
    return mc.connect(
        host="localhost",
        database="employees",
        user="root",
        password="Rameshsurya@08"
    )
def log(data):
    """Login route to check username and password."""
    try:
        db = get_db_connection()
        cursor = db.cursor()

        # Get data from POST request body
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required!"}), 400

        query = """
        SELECT * FROM employees_users WHERE username = %s AND password = %s
        """
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            return jsonify({"message": "User successfully logged in"})
        else:
            return jsonify({"error": "Invalid username or password"}), 400

    except Error as er:
        return jsonify({"error": f"An error occurred: {str(er)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

def for_pass(data):
    """Update password route."""
    try:
        db = get_db_connection()
        cursor = db.cursor()

        # Get data from POST request body
        data = request.get_json()
        user_name = data.get("username")
        new_pass = data.get("new_password")
        conf_pass = data.get("confirm_password")

        if not user_name or not new_pass or not conf_pass:
            return jsonify({"error": "All fields are required!"}), 400

        if new_pass != conf_pass:
            return jsonify({"error": "Passwords do not match!"}), 400

        check_un = "SELECT * FROM employees_users WHERE username = %s"
        cursor.execute(check_un, (user_name,))
        result = cursor.fetchone()

        if result:
            query = "UPDATE employees_users SET password = %s WHERE username = %s"
            cursor.execute(query, (new_pass, user_name))
            db.commit()

            if cursor.rowcount > 0:
                return jsonify({"message": "Password has been updated successfully!"})
            else:
                return jsonify({"error": "Failed to update password!"}), 500
        else:
            return jsonify({"error": "Username not found!"}), 400

    except Error as er:
        return jsonify({"error": f"An error occurred: {str(er)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

def for_un(data):
    """Update username route."""
    try:
        db = get_db_connection()
        cursor = db.cursor()

        # Get data from POST request body
        data = request.get_json()
        email = data.get("email")
        new_un = data.get("new_username")
        conf_un = data.get("confirm_username")

        if not email or not new_un or not conf_un:
            return jsonify({"error": "All fields are required!"}), 400

        if new_un != conf_un:
            return jsonify({"error": "Usernames do not match!"}), 400

        check_un = "SELECT * FROM employees_users WHERE email = %s"
        cursor.execute(check_un, (email,))
        result = cursor.fetchone()

        if result:
            query = "UPDATE employees_users SET username = %s WHERE email = %s"
            cursor.execute(query, (new_un, email))
            db.commit()

            if cursor.rowcount > 0:
                return jsonify({"message": "Username has been updated successfully!"})
            else:
                return jsonify({"error": "Failed to update username!"}), 500
        else:
            return jsonify({"error": "Email not found!"}), 400

    except Error as er:
        return jsonify({"error": f"An error occurred: {str(er)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

if __name__ == "__main__":
    app.run(debug=True)
