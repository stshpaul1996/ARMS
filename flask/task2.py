from flask import Flask, jsonify
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database connection configuration (replace with your actual database details)
DATABASE_URL = 'postgresql://postgres:root@localhost/blog'
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Assuming you have a 'role_permissions' table in your database
meta = MetaData()
role_permissions = Table('role_permissions', meta, autoload_with=engine)

@app.route('/get-role-permissions', methods=['GET'])
def get_role_permissions():
    try:
        # Query to retrieve all role permissions
        query = session.query(role_permissions).all()

        # Create a dictionary with name as the key and id as the value
        permissions = {row.name: row.id for row in query}

        # Return the dictionary as a JSON response
        return jsonify(permissions)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
