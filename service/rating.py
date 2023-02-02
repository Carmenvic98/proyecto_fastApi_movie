from models.rating import Rating as RatingModel
from schemas.rating import Rating

class RatingService():

    def __init__(self,db) -> None:
        self.db = db

    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result

    def get_rating(self, rev_id:int):
        result = self.db.query(RatingModel).filter(RatingModel.rev_id == rev_id).first()
        return result
    
    def get_rating_by_rev_stars(self, rev_stars:int):
        result = self.db.query(RatingModel).filter(RatingModel.rev_stars == rev_stars).all()
        return result
    
    def create_rating(self, rating:Rating):
        new_rating = RatingModel(
            movie_id= rating.movie_id,
            rev_id= rating.rev_id,
            rev_stars= rating.rev_stars,
            num_o_ratings= rating.num_o_ratings
        )
        self.db.add(new_rating)
        self.db.commit()
        return
    
    def update_rating(self, num_o_ratings:int, data:Rating):
        rating.movie_id = data.movie_id
        rating.rev_id = data.rev_id
        rating.rev_stars = data.rev_stars
        rating = self.db.query(RatingModel).filter(RatingModel.num_o_ratings == num_o_ratings).first()
        self.db.commit()
        return
    
    def delete_rating(self, rev_id:int):
        self.db.query(RatingModel).filter(RatingModel.rev_id == rev_id).delete()
        self.db.commit()
        return