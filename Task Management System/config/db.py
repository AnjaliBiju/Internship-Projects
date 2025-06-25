import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port= 3306,
        user= "root",
        password="Anjali@3011",
        database= "TaskManagerDB"
    )
    
if __name__=="__main__":
    try:
        conn= get_connection()
        print("Connection successful");
        conn.close()
    except Exception as e:
        print("Connection failed: ",e)