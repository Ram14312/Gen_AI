from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

db_url = "postgresql://neondb_owner:npg_S50wnvekCBDI@ep-curly-bread-anssibzt-pooler.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

#for schema vaildation for an post api we use pydantic and this base model inorder to define
#each filed as a specific datatype

class Student(BaseModel):
    id:int
    name:str
    age:int

#for db connectivity we need to install something by below command
#python -m pip install psycopg2-binary

def get_connection_url():
    conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
    return conn;


#now we are creating a function to store the data into the file which were posted in api
def save_student_to_file(data):
    with open("students.txt", "a") as f:
        f.write(f"{data.id}, {data.name}, {data.age}\n")


#now in the post api we are calling the methd for to save the file and passing data in dictionary format

@app.post("/add_student")
def create_student(stud: Student ):
    save_student_to_file(stud)
    return {"message": "student data saved successfully"}

#now we are going to use neondb which is as similar to h2db for java which virtual db based on sql
#postgresql://neondb_owner:npg_S50wnvekCBDI@ep-curly-bread-anssibzt.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require
#npx neonctl@latest init
#brew install neonctl && neonctl init

#inorder to connect to database and later it need to store the data from the api to database for that we need to go with below func
@app.post("/students/db/insert")
def store_student_in_db(student: Student):
    conn = get_connection_url()
    cursor = conn.cursor()
    insert_query = "INSERT INTO student (id,name, age) values (%s, %s, %s)"
    cursor.execute(insert_query, (student.id, student.name, student.age))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "data is persisted in the db successfully"}

@app.put("/students/db/update/{id}")
def store_student_in_db(id:int,student: Student):
    conn = get_connection_url()
    cursor = conn.cursor()
    update_query = '''Update student 
                    set  name= %s , age =%s 
                    where id = %s''' 
    cursor.execute(update_query, ( student.name, student.age, id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Updated the record in the db successfully"}

@app.delete("/students/db/delete/{id}")
def store_student_in_db(id:int):
    conn = get_connection_url()
    cursor = conn.cursor()
    delete_query = "DELETE FROM student where id =%s"
    cursor.execute(delete_query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "deleted a row in the db successfully"}