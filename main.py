from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import json
app = FastAPI()


f = open('data.json')
data = json.load(f)

class Students(BaseModel):
    name: str | None = None
    description: str | None = None

class Teachers(BaseModel):
    name: str | None = None
    classe: str | None = None

class Courses (BaseModel):
    name: str | None = None
    description: str | None = None
    price: int | None = None

class Cafe (BaseModel):
    name: str | None = None
    sugar: bool | None = False

class Bootcamp(BaseModel):
    students:list [Students]  | None = None
    teachers: list [Teachers] | None = None
    courses: list[Courses] | None = None
    cafe: list[Cafe] | None = None

def getElement(name, bootcamp_el):
    for el in bootcamp_el:
        if el['name'] == name:
            return el
    return None 

@app.get("/")
async def Welcome():
    return {"message": "Welcome to Basetis"}


@app.get("/bootcamp/", response_model=Bootcamp)
async def read_item():
    return data['bootcamp']

@app.get("/courses/{courses_id}", response_model=Courses)
async def read_course(courses_id: str):
    element = getElement(courses_id, data['bootcamp']['courses'])
    if not element:
         raise HTTPException(status_code=404, detail="Item not found")
    return element

@app.get("/students/{students_id}", response_model=Students)
async def read_student(students_id: str):
    element = getElement(students_id, data['bootcamp']['students'])
    if not element:
         raise HTTPException(status_code=404, detail="Item not found")
    return element

@app.post("/students/")
async def create_student(students: Students):
    post_item_encoded = jsonable_encoder(students)
    data['bootcamp']['students'].append(post_item_encoded)
    return data['bootcamp']


@app.get("/teachers/{teacher_id}", response_model=Teachers)
async def read_student(teacher_id: str):
    element = getElement(teacher_id, data['bootcamp']['teachers'])
    if not element:
         raise HTTPException(status_code=404, detail="Item not found")
    return element

@app.post("/teachers/")
async def create_student(teachers: Teachers):
    post_item_encoded = jsonable_encoder(teachers)
    data['bootcamp']['teachers'].append(post_item_encoded)
    return data['bootcamp']

@app.put("/courses/{courses_id}", response_model=Courses)
async def update_courses(courses_name: str, item: Courses):
    element = getElement(courses_name, data['bootcamp']['courses'])
    if not element:
         raise HTTPException(status_code=404, detail="Item not found")
    id = data['bootcamp']['courses'].index(element) 
    update_item_encoded = jsonable_encoder(item)
    data['bootcamp']['courses'][id] = update_item_encoded
    return update_item_encoded

@app.delete("/delete/{courses_id}")
async def remove_course(courses_id : str):
    element = getElement(courses_id, data['bootcamp']['courses'])
    if not element:
         raise HTTPException(status_code=404, detail="Item not found")
    id = data['bootcamp']['courses'].index(element)
    del data['bootcamp']['courses'][id]
    delete_message = str("Course deleted correctly")
    return delete_message

f.close()