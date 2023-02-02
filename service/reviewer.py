from models.reviewer import Reviewer as ReviewerModel
from schemas.reviewer import Reviewer

class ReviewerService():

    def __init__(self,db) -> None:
        self.db = db

    def get_reviewer(self):
        result = self.db.query(ReviewerModel).all()
        return result
    
    def get_reviewer(self, id:int):
        result = self.db.query(ReviewerModel).filter(ReviewerModel.id == id).first()
        return result
    
    def get_reviewer_by_name(self, name:str):
        result = self.db.query(ReviewerModel).filter(ReviewerModel.name == name).all()
        return result