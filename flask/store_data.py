import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Database connection configuration
DATABASE_URL = 'postgresql://postgres:root@localhost/blog'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define a function to create the table dynamically if it doesn't exist
def create_table(metadata, table_name, columns_dict):
    columns = [Column('id', Integer, primary_key=True, autoincrement=True)]
    
    # Dynamically create columns from the dictionary keys
    for key, value in columns_dict.items():
        columns.append(Column(key, String(255)))  # Assuming all values are strings, you can change the type based on your needs

    # Create the table object
    table = Table(table_name, metadata, *columns, extend_existing=True)
    
    # Create the table in the database
    metadata.create_all(engine)
    
    return table

# Insert data into the table
def insert_data(table, data_dict):
    insert_query = table.insert().values(data_dict)
    session.execute(insert_query)
    session.commit()
    print("Data inserted successfully!")

# Main function to run the script
def main():
    try:
        # Dictionary where keys are column names and values are the corresponding data
        data = {
            "name": "shravan dasari",
            "email": "shravan.1996@example.com",
            "role": "HR"
        }

        # Metadata object to hold the schema
        metadata = MetaData()

        # Table name
        table_name = "users"

        # Create the table dynamically if it doesn't exist
        table = create_table(metadata, table_name, data)

        # Insert data into the table
        insert_data(table, data)

    except Exception as e:
        session.rollback()  # Rollback in case of error
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
