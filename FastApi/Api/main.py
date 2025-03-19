from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fakedb = []

class courses(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Greetings welcome": "Welcome"}

@app.get("/courses")
def get_Courses():
    return fakedb

@app.get("/courses/{course_id}")
def get_a_course(course_id:int):
    course = course_id - 1
    return fakedb(course)

@app.post("/courses")
def add_a_course(courses:courses):
    fakedb.append(courses.dict())
    return fakedb[-1]

@app.delete("/courses/{course_id}")
def delete_course(course_id:int):
    fakedb.pop(course_id - 1)
    return{"Task": "Deletion Successful"}