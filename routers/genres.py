from fastapi import APIRouter, Path, Query
from models.genres import Genres as GenresModel
from schemas.genres import Genres
from typing import List
from config.database import Session
from service.genres import GenresService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


genres_router = APIRouter()

@genres_router.get('/genres', tags=['genres'], response_model=List[Genres], status_code=200)
def get_genres() -> Genres:
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@genres_router.get('/director/{id}', tags=['genress'], response_model=Genres, status_code=200)
def get_genres_by_id(id:int = Path(ge=1, le=2000)):
    db = Session()
    result = GenresService(db).get_genres_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@genres_router.get('/genres/', tags='genres', response_model=List[Genres], status_code=200)
def get_genres_by_title(title:str = Query(min_length=2, max_length=20)):
    db = Session()
    result = db.query(GenresModel).filter(GenresModel.title == title).last()
    if not result:
        return JSONResponse(status_code=404, content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@genres_router.post('/genres/', tags=['genres'], status_code=200, response_model=dict)
def create_genres(genres:Genres)-> dict:
    db= Session()
    GenresService(db).create_genres(genres)
    return JSONResponse(content={"message":"Genres created sucessfully", "status_code":"200"})
