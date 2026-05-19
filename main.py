#pip install fastapi
#pip install uvicorn (inorder to run the fastapi)
# if pip is installed in c drive then in d drive will get exception to fix this use python -m as prefix)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def my_func():
    return {"message": "this is ram"}

#now in order to get that statement to be printed will go with a sbelow statement
my_func() # this is pythonic way of calling the function

@app.get("/ram")
def test():
    return "this ram an ai genaralist"

#now currently our requirement is we need to call an api to get output of the function instead of calling it in pythonic way

# now the requirement a sdiscussed in the previous class about the gpay app how it is connected with different bank servers
# and how all the users can use it and internally how the communication is going with different technology were able to access this

# with some set of rule i am going to expose this function to be called by everyone where api plays a key role here

#here fastapi library comes into the picture

# we have flask framework as well but it is used not used for production grade applications

#for to this first import the fastapi
#create fastapi object
# later decorate it with @app.get("/")
#now any can able to access this

#inorder to execute this we need to use uvicorn filename: app (variable)
#after running will get output as uvicorn is running on some server url detail

#if anyone wnats to access the function they need to reach to 127.0.0.1 (local system): 8080 (port) , until the server is running

# python -m uvicorn main:app --reload use this command for to execute it
# whenever we are making a new change we need to restrat the command then only we can able to see the changes

# suppose w e are doing continous development then we need to change command as main:app --relaod

#now the api is running in my local system if someone want to access how can they are going to access it?
# for this we can expose the api to the world with the help of service provider called as "ngrok" but its a temporary solution

# for to give access to someone inorder to access the things in our system  in that situation we can use ngrok service provider


#ngrok config add-authtoken 1c3u8tXWVxwWLjsh9OBUrt0ibJG_3U8eXWeuRq8tkPnoPzPvj
#copy the above in ngrok

#to expose the app running in port 8000 need to follow below steps

# command : ngrok http 8000

#  https://6a84-2405-201-c04b-80a8-e441-a818-bee3-d148.ngrok-free.app  will get this output after running above command

# anyone who is using above url can able to access my two functions

#now if the url is accessed from any any system they can able to access this


#lets suppose

students = {1:"ram", 2: "remo", 3: "rambo"}

#if someone is aksing try to create an api by which anyone can able to access student data

@app.get("/students")
def get_student():
    return students

#now we can access with ngrok and using localsystem url as well

#i wanted to access a student data by taking student id as input it should return specific record from the api

@app.get("/students/{studentId}")
def get_student_detail(studentId:int):
    return {"id":studentId , "name":students[studentId]}

#in the api router if anything is closed with curly braces {} i.e the api is expecting the input
#the above logic works only after making studnetId: int because initially the python considers as string so will get internal server error

#the next requiremnet is to add a new record into the dictionary via api

#@app.get("/add_student/{studentId}/{name}")
@app.get("/add_student")
def add_student(studentId:int , name:str):
    students[studentId] = name
    return  students

#for above function we can use @app.get("/add_student/{studentId}/{name}") or @app.get("/add_student")
#for second one url we can passdata after calling the api like localhost:8000/add_student?studentId=4&name=ram

#post approach how can we add student  will look below


#how now we are going to use post api
#for example login into some account in which in the url we cannot see the parameters which we pass like username and passwrd as similar to get api'
#the post api is not going to hit directly from url
# for get api example think about google search
#for post api think about example as gmail account login

@app.post("/add_student_diff")
def add_student_diff():
    students['new_id'] = "new_name"
    return students

#so in the url we cannot hit this post api instead we can use postman to hit this post api
#if we hit the same api in url then will get output as method not allowed
#in the above post method we have sent the hardcorded value

#now the requirement we need to pass the our required values without hardcording i.e id and name
from pydantic import BaseModel

class newdata(BaseModel):
    studentId:int
    name:str

@app.post("/add_student_new_value")
def add_student_new_value(student:newdata):
     students[student.studentId] = student.name
     return students

     







