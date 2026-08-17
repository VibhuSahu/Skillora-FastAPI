from app.db import UserCommentDB
from app.models.UserCommentModel import UserCommentModel
from pydantic import UUID4


# services
from app.services.userCommentService.replaceData import change_course_id, change_user_id, change_parent_comment, change_content


# CRUD

# Creat
def addUserCommentToDB(data: UserCommentModel) -> None:
    UserCommentDB.append(data)
            

# Read 
def getAllUserComments() -> list[UserCommentModel]:
    return UserCommentDB


# Read
def getUserCommentById(user_id: UUID4) -> UserCommentModel:
    for user in UserCommentDB:
        if user.commentid == user_id:
            return user
    raise ValueError("Comment not Exit")


# Update        
def replaceUserCommentById(user_id: UUID4, data: UserCommentModel) -> UserCommentModel:
    
    for index, comment in enumerate(UserCommentDB):
        if comment.commentid == user_id:
            UserCommentDB[index] = data
            return data

    raise ValueError("Comment Not Exist")
        
# Update
def updateUserCommentById(user_id: UUID4, field: str, data: str) -> UserCommentModel:
    match field:
        case "course_id":
            return change_course_id(user_id, data)
        case "user_id":
            return change_user_id(user_id, data)
        case "parent_comment":
            return change_parent_comment(user_id, data)
        case "content":
            return change_content(user_id, data)
        case _:
            raise ValueError("Field not Exit")
            
            
# Delete
def deleteUserCommentById(user_id: UUID4) -> bool:
    for user in UserCommentDB:
        if user.commentid == user_id:
            UserCommentDB.remove(user)
            return True
    
    raise ValueError("Comment Not Exit")
    

 