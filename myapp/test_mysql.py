import mysql.connector

# Replace the values below with your MySQL container's configuration
host = 'localhost'
port = '3306'
user = 'root'
password = 'secret'
database = 'mysql'

try:
    # Connect to the MySQL database
    cnx = mysql.connector.connect(
        user=user, password=password, host=host, port=port, database=database)

    # Print a success message if the connection was successful
    if cnx.is_connected():
        print('Connected to MySQL database!')

     # Get a cursor object to execute queries
        cursor = cnx.cursor()

        # Execute a query to get all table names
        cursor.execute("SHOW TABLES")

        # Fetch all results and print them
        tables = cursor.fetchall()
        print('Tables in the database:')
        for table in tables:
            print(table[0])

except mysql.connector.Error as err:
    # Print an error message if the connection was unsuccessful
    print(f'Error connecting to MySQL database: {err}')

finally:
    # Close the database connection
    cnx.close()
