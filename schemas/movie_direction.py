from pydantic import BaseModel

class Movie_direction(BaseModel):

    dir_id: int
    movie_id: int

    class Config:
        schema_extra={
            "example":{
                'dir_id': 2,
                'movie_id': 4,
            }
        }