import psycopg2
from psycopg2 import sql
import sys

DATABASE = "A3Q1"
USER = "postgres"
PASSWORD = "Kuwait$22"
HOST = "localhost"
PORT = "5432"

def connect_db():
    try:
        conn = psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def getAllStudents():
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students;")
        records = cur.fetchall()
        for row in records:
            print(row)
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect_db()
    with conn.cursor() as cur:
        try:
            cur.execute(sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"),
                        (first_name, last_name, email, enrollment_date))
            conn.commit()
            print("Student added successfully.")
        except psycopg2.Error as e:
            print(f"Failed to add student: {e}")
            conn.rollback()
    conn.close()

def updateStudentEmail(student_id, new_email):
    conn = connect_db()
    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
            conn.commit()
            print("Email updated successfully.")
        except psycopg2.Error as e:
            print(f"Failed to update email: {e}")
            conn.rollback()
    conn.close()

def deleteStudent(student_id):
    conn = connect_db()
    with conn.cursor() as cur:
        try:
            cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
            conn.commit()
            print("Student deleted successfully.")
        except psycopg2.Error as e:
            print(f"Failed to delete student: {e}")
            conn.rollback()
    conn.close()

if __name__ == "__main__":
    getAllStudents()
    #addStudent('Alice', 'Wonderland', 'alice@example.com', '2023-09-03')
    #updateStudentEmail(1, 'new.email@example.com')
    #getAllStudents()
    # deleteStudent(3)