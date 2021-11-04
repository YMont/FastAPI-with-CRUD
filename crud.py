from typing import List
from fastapi.exceptions import HTTPException
from sql_app import model
from sqlalchemy.orm import Session, session
from sql_app.model import PeopleInfo
from sql_app.schemas import PeopleBase, PeopleUpdate, PeopleType

# get(Create), post(Read), put(Update, delete(Delete)

def get_user_by_id(boxSession: Session, _id: int):
    return boxSession.query(PeopleInfo).filter(PeopleInfo.id == _id).first()

def get_users(boxSession: Session, _skip: int=0, _limit: int=100) -> List[PeopleInfo]:
    return boxSession.query(PeopleInfo).offset(_skip).limit(_limit).all()

def create_user(boxSession: Session, _createData: PeopleUpdate) -> PeopleInfo :
    peopleDetail = boxSession.query(PeopleInfo).filter(PeopleInfo.name == _createData.name,
                                                        PeopleInfo.height == _createData.height,
                                                        PeopleInfo.weight == _createData.weight,
                                                        PeopleInfo.habbit == _createData.habbit).first()
    if peopleDetail is not None:
        raise HTTPException(status_code=409, detail="People already exist.")
    
    newPeopleInfo = PeopleInfo(**_createData.dict())
    boxSession.add(newPeopleInfo)
    boxSession.commit()
    boxSession.refresh(newPeopleInfo)
    return newPeopleInfo

def update_user(boxSession: Session, _id: int , infoUpdate: PeopleUpdate) -> PeopleInfo:
    orignalInfo = get_user_by_id(boxSession, _id)

    if orignalInfo is None:
        raise HTTPException(status_code=404 , detail="404 Not Found.")
    
    orignalInfo.name = infoUpdate.name
    orignalInfo.height = infoUpdate.height
    orignalInfo.weight = infoUpdate.weight
    orignalInfo.habbit = infoUpdate.habbit
    boxSession.commit()
    boxSession.refresh(orignalInfo)

    return orignalInfo


def delete_user(boxSession: Session, _id: int):
    res = get_user_by_id(boxSession, _id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    boxSession.delete(res)
    boxSession.commit()
    return { "code": 0 }
