from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sql_app import crud, model
from sql_app.schemas import PeopleType, PeopleUpdate
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm.session import Session

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/user/{user_id}",response_model=PeopleUpdate)
def read_user_id(user_id: int, db:Session= Depends(get_db)):
    res = crud.get_user_by_id(db,user_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res

@app.get("/users/",response_model=PeopleType)
def read_users(skip: int=0, limit: int=100, db:Session= Depends(get_db)):
    res = crud.get_users(db, skip, limit)
    response = {"skip":skip , "limit":limit , "data":res}
    return response

@app.post("/users/",response_model=PeopleUpdate)
def create_user(userForm: PeopleUpdate, db:Session= Depends(get_db)):
    try:
        res = crud.create_user(db, userForm)
        return res
    except Exception as err:
        return HTTPException(**err.__dict__)

@app.put("/user/{user_id}", response_model=PeopleUpdate)
def update_user(userForm: PeopleUpdate, user_id: int, db:Session= Depends(get_db)):
    try:
        res = crud.update_user(db, user_id, userForm)
        return res
    except Exception as err:
        raise HTTPException(**err.__dict__)

@app.delete("/user/{user_id}")
def delete_user(user_id: int, db:Session= Depends(get_db)):
    try:
        crud.delete_user(db,user_id)
    except Exception as err:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return {"code": 0}
