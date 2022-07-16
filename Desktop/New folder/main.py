from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database
import models

app = FastAPI()


@app.get("/day2/{id}")
def get_user(id: int, db: Session = Depends(database.get_db)):
    data = db.query(models.day2).filter(models.day2.Id == id).first()
    return {"data": data}
   
@app.post("/person")
def add_person(username:str,
password: str,
Email: str,
blog_id: int,
db:Session = Depends(database.get_db)):
    data=models.person(person_username=username,
                     person_password =password, person_email=Email,blog_id=blog_id)
    db.add(data)    
    db.commit()

# get method is use to readdata
@app.get("/person/{id}")
def get_person_by_id(id: int , db: Session = Depends(database.get_db)):
  data = db.query(models.person).filter(models.person.person_id == id).first()
  return {"status":200 , "message": "Data Found", "data": data}
