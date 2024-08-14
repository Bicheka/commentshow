from pydantic import BaseModel

class Show(BaseModel):
    name: str # TODO create an index to search for show name more efficiently
    comment_count: int
    calification: int # TODO make sure it is withing a range example (0-10) or (0-5) including the last number
    episodes_count: int
    
    # TODO add image
    
    
    