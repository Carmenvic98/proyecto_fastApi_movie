from pydantic import BaseModel, Field
from typing import Optional

class Reviewer(BaseModel):

    id: Optional[int]= None
    name: str= Field(max_lenght=25, min_lenght=3)

    class Config:
        schema_extra={
            "example":{
                'id': 6,
                'name': 'Hannah Steele'
            }
        }