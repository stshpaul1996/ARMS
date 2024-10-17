from flask import Flask, send_file, jsonify
from io import BytesIO
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

# Configure your database connection (replace with your actual DB URL)
DATABASE_URL = 'postgresql://postgres:root@localhost/blog'
engine = create_engine(DATABASE_URL)

# Route to download data as an Excel file
@app.route('/download-excel', methods=['GET'])
def download_excel():
    try:
        # Query the database (replace 'your_table' with your actual table)
        query = "SELECT * FROM blog"
        df = pd.read_sql(query, engine)
        
        # Create a BytesIO buffer to save the Excel file
        output = BytesIO()

        # Write the DataFrame to Excel in-memory
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Rewind the buffer
        output.seek(0)

        # Send the Excel file for download
        return send_file(output, as_attachment=True, download_name='data.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
