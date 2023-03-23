from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import json
app = FastAPI()


f = open('data.json')
data = json.load(f)
print(data['bootcamp'])

class Students(BaseModel):
    name: str | None = None
    description: str | None = None

class Teacher(BaseModel):
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
    teachers: list [Teacher] | None = None
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
async def read_item(courses_id: str):
    element = getElement(courses_id, data['bootcamp']['courses'])
    if not element:
         raise HTTPException(status_code=404, detail="Item not found")
    return element

@app.post("/students/")
async def create_user(user_id: str, students: Students):
    post_item_encoded = jsonable_encoder(students)
    data['bootcamp']['courses']= post_item_encoded
    return post_item_encoded

@app.post("/teacher/")
async def create_teacher(teacher: Teacher):
    return teacher

f.close()
'''
@app.put("/courses/{courses_id}", response_model=Courses)
async def update_courses(courses_name: str, item: Courses):
    update_item_encoded = jsonable_encoder(item)
    data['bootcamp']['courses'][] = update_item_encoded
    return update_item_encoded
'''