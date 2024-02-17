from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import pymysql.cursors

app = Flask(__name__)


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin@123'
app.config['MYSQL_DATABASE_DB'] = 'PyCarRent'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
mysql.init_app(app)


@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data['username']
    password = data['password']
    email = data['email']
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data['username']
    password = data['password']
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            return jsonify({"message": "Login successful", "user": user}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.json
    make = data['make']
    model = data['model']
    year = data['year']
    registration_number = data['registration_number']
    daily_rate = data['daily_rate']
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vehicles (make, model, year, registration_number, daily_rate) VALUES (%s, %s, %s, %s, %s)",
                       (make, model, year, registration_number, daily_rate))
        conn.commit()
        return jsonify({"message": "Vehicle added successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route('/vehicles', methods=['GET'])
def list_vehicles():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vehicles")
        vehicles = cursor.fetchall()
        return jsonify(vehicles), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route('/rentals/book', methods=['POST'])
def book_rental():
    data = request.json
    user_id = data['user_id']
    vehicle_id = data['vehicle_id']
    start_date = data['start_date']
    end_date = data['end_date']
    total_cost = data['total_cost']
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rentals (user_id, vehicle_id, start_date, end_date, total_cost) VALUES (%s, %s, %s, %s, %s)",
                       (user_id, vehicle_id, start_date, end_date, total_cost))
        conn.commit()
        return jsonify({"message": "Rental booked successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route('/users/profile', methods=['PUT'])
def update_profile():
    data = request.json
    user_id = data['user_id']
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username = %s, password = %s, email = %s WHERE user_id = %s",
                       (username, password, email, user_id))
        conn.commit()
        return jsonify({"message": "Profile updated successfully"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
