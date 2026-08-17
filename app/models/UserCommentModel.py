from datetime import date
from pydantic import BaseModel, UUID4, Field
from typing import Optional
 
 
class UserCommentModel(BaseModel):
    commentid: UUID4
    course_id: UUID4
    user_id: UUID4
    parent_comment:  Optional[UUID4] = None
    content: str = Field(min_length=0, max_length=200)
    created_at: date
    
 

 