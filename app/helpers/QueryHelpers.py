
from mysql.connector import Error
from connection.db import get_db_connection 
from helpers.HelperFunction import responseData
# Function to execute a POST query (Insert/Update/Delete)
def executePost(query, params=()):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        # Execute the provided query with parameters
        cursor.execute(query, params)
        
        # Commit changes for INSERT/UPDATE/DELETE
        conn.commit()
        # Get the last inserted ID if it was an INSERT query
        last_inserted_id = cursor.lastrowid
        # Return the number of affected rows
        # Return the last inserted ID and the number of affected rows
        return {"last_inserted_id": last_inserted_id, "rowcount": cursor.rowcount}
    except Error as e:
        # Successful signup response
        return responseData("success", "An error occurred: {e}", "", 200)
        
    finally:
        # Close the database connection
        if conn.is_connected():
            cursor.close()
            conn.close()



# Function to execute a GET query (Select)
def executeGet(query, params=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        # Execute the provided query with parameters
        cursor.execute(query, params or [])
        
        # Fetch all results
        rows = cursor.fetchall()
        return rows
    except Error as e:
        return responseData("success", "An error occurred: {e}", "", 200)
    finally:
        # Close the database connection
        if conn.is_connected():
            cursor.close()
            conn.close()

def changeStatus(table_name, id_field, value_id, status_to):
    query = f"UPDATE {table_name} SET status = %s WHERE {id_field} = %s"
    try:
        result = executePost(query, (status_to, value_id))
        if result:  # Check if the result indicates success
            return True
        return False
    except Exception as e:
        print(f"Error: {str(e)}")  # Optionally log the error for debugging
        return responseData("error", "Something went wrong!", "", 200)
    
def changeRole(table_name, id_field, value_id, status_to):
    query = f"UPDATE {table_name} SET role_id = %s WHERE {id_field} = %s"
    try:
        result = executePost(query, (status_to, value_id))
        if result:  # Check if the result indicates success
            return True
        return False
    except Exception as e:
        print(f"Error: {str(e)}")  # Optionally log the error for debugging
        return responseData("error", "Something went wrong!", "", 200)