from pydantic import BaseModel, field_validator
from datetime import datetime

class Comment(BaseModel):
    content: str
    show_id: str
    user_id: str
    date_created: datetime # example 2032-04-23T10:20:30.400+02:30
    username: str
    reply_count: int  # TODO ensure it is >= 0
    @field_validator('content')
    def name_must_contain_space(cls, v):
        if len(v) > 300:
            raise ValueError('must be less than 100 digits long')
        return v
        