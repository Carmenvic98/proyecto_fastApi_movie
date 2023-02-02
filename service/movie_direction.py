from models.movie_direction import Movie_direction as MovieDirectionModel
from schemas.movie_direction import Movie_direction

class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movies_direction(self):
        result = self.db.query(MovieDirectionModel).all()
        return result
    
    def get_movie_direction(self, dir_id:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.dir_id == dir_id).first()
        return result
    
    def get_movies_direction_by_movie_id(self, movie_id:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.movie_id == movie_id).all()
        return result
    
    def create_movie_direction(self, movie_direction:Movie_direction):
        new_movie_direction = MovieDirectionModel (
            dir_id= movie_direction.dir_id,
            movie_id= movie_direction.movie_id
        )
        self.db.add(new_movie_direction)
        self.db.commit()

    def update_movie_direction(self, movie_id:int, data:Movie_direction):
        movie_direction.dir_id = data.dir_id
        movie_direction = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.movie_id == movie_id).first()
        self.db.commit()
        return
    
    def delete_movie_direction(self, dir_id:int):
        self.db.query(MovieDirectionModel).filter(MovieDirectionModel.dir_id == dir_id).delete()
        self.db.commit()
        return
