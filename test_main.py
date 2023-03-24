from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() ==    {"message": "Welcome to Basetis"}


def test_courses():
    response = client.get("/courses/SCRUM")
    assert response.status_code == 200
    assert response.json() == {"name": "SCRUM", "description": "S.C.R.U.M.","price": 99}

def test_courses():
    response = client.get("/students/Laura")
    assert response.status_code == 200
    assert response.json() == {"name": "Laura", "description": "Arribas"}
    '''
def test_put_course_default():
    response = client.put(
        "/courses/SCRUM",
        headers={"X-Token": "coneofsilence"},
        json=[{
            "name": "FastAPI", 
            "description": "Very Fast", 
            "price": 1234
        }],
    )  
    #assert response.status_code == 200

    assert response.json() == {
    "name": "string",
    "description": "string",
    "price": 0
    }
    '''

def test_delete_course():
    response = client.delete("/delete/SCRUM")
    assert response.status_code == 200
    assert response.json() == "Course deleted correctly"


    '''
def test_bootcamp():
    response = client.get("/bootcamp")
    assert response.status_code == 200
    assert response.json() ==    {  
        "students" : [
            {"name": "Alex", "description": "Informatic"},
            {"name": "Lorena", "description": "Gatos"},
            {"name": "Enaitz", "description": "Nadador"},
            {"name": "Laura", "description": "Arribas"}
        ],   
        "teachers" : [
            {"name": "Edgar", "classe": "Accesibilidad"},
            {"name": "Gabriel", "classe": "FastApi"},
            {"name": "Francesc", "classe": "SCRUM"}
        ],
        "courses" : [   
            {"name": "SCRUM", "description": "S.C.R.U.M.","price": 99},
            {"name": "FastAPI", "description": "Very Fast", "price": 1234},
            {"name": "Accesibilidad", "description": "Que lo pueda leer bien.", "price": 365}
        ], 
        "cafe" : [
            {"name": "Decaf", "sugar": "False"},
            {"name": "Ristretto", "sugar": "False"},
            {"name": "Intenso", "sugar": "True"}
        ]
    }
'''