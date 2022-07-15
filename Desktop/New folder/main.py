from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database
import models


app = FastAPI()


@app.get("/day2/{id}")
def get_user(id: int, db: Session = Depends(database.get_db)):
    data = db.query(models.day2).filter(models.day2.Id == id).first()
    return {"data": data}
