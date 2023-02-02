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
    
    def create_reviewer(self, reviewer:Reviewer):
        new_reviewer = ReviewerModel(
            id= reviewer.id,
            name= reviewer.name
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return
    
    def update_reviewer(self, name:str, data:Reviewer):
        reviewer.id = data.id
        reviewer = self.db.query(ReviewerModel).filter(ReviewerModel.name == name).first()
        self.db.commit()
        return
    
    def delete_reviewer(self, id:int):
        self.db.query(ReviewerModel).filter(ReviewerModel.id == id).delete()
        self.db.commit()
        return
        