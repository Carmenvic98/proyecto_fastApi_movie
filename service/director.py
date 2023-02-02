from models.director import Director as DirectorModel
from schemas.director import Director

class DirectorService():
    
    def __init__(self,db) -> None:
        self.db = db

    def get_director(self):
        result = self.db.query(DirectorModel).all()
        return result
    
    def get_director(self, fname:str):
        result = self.db.query(DirectorModel).filter(DirectorModel.fname == fname).first()
        return result
    
    def get_director_by_lname(self, lname:str):
        result = self.db.query(DirectorModel).filter(DirectorModel.lname == lname).all()
        return result
    
    def create_director(self, director:Director):
        new_director = DirectorModel(
            id= director.id,
            fname= director.fname,
            lname= director.lname
        )
        self.db.add(new_director)
        self.db.commit()
        return
    
    def update_director(self, id:int, data:Director):
        director = self.db.query(DirectorModel).filter(DirectorModel.id == id).first()
        director.fname = data.fname
        director.lname = data.lname
        self.db.commit()
        return
    
    def delete_director(self, fname:str):
        self.db.query(DirectorModel).filter(DirectorModel.fname == fname).delete()
        self.db.commit()
        return
        