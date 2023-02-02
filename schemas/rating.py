from pydantic import BaseModel

class Rating(BaseModel):
    movie_id: int
    rev_id: int
    rev_stars: int
    num_o_ratings: int

    class Config:
        schema_extra={
            "example":{
                'movie_id': 4,
                'rev_id': 5,
                'rev_stars': 3,
                'num_o_ratings': 4,
            }
        }