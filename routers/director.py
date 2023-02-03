from fastapi import APIRouter, Query
from models.director import Director as DirectorModel
from schemas.director import Director
from typing import List
from config.database import Session
from service.director import DirectorService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder




director_router = APIRouter()

@director_router.get('/director', tags=['director'], response_model=List[Director], status_code=200)
def get_directors() -> Director:
    db = Session()
    result = DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.get('/director/', tags=['director'], response_model=Director, status_code=200)
def get_director_by_fname(fname:str = Query(min_length=5, max_length=20)):
    db = Session()
    result = db.query(DirectorModel).filter(DirectorModel.fname == fname).first()
    if not result:
        return JSONResponse(status_code=400, content={"message":"No found director with that first name"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.get('/director/', tags=['director'], response_model=List[Director], status_code=200)
def get_director_by_lname(lname:str = Query(min_length=1, max_length=20)):
    db = Session()
    result = db.query(DirectorModel).filter(DirectorModel.lname == lname).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.post('/director/', tags=['director'], status_code=200, response_model=dict)
def create_director(director:Director)-> dict:
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={"message": "Director created sucessfully.", "status_code":200})

@director_router.put('/director/{id}', tags=['director'])
def update_director(id:int, director:Director):
    db = Session()
    result = DirectorService(db).update_director(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro", "status_code":"404"})
    DirectorService(db).update_director(id.director)
    return JSONResponse(content={"message":"Se ha modificado el id exitosamente"})

@director_router.delete('/director/{fname}', tags=['director'])
def delete_director(fname:str):
    db = Session()
    result = DirectorService(db).delete_director(fname)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content="Delete director", status_code=200)
