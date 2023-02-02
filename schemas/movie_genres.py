from pydantic import BaseModel

class MoviesGenres(BaseModel):

    movie_id: int
    gen_id: int

    class Config:
        schemas_extra={
            "example":{
                'movie_id': 2,
                'gen_id': 3,
            }
        }