from fastapi import APIRouter, HTTPException
from pydantic import UUID4

from app.models.UserCommentModel import UserCommentModel
from app.controllers.userCommentController import (
    addUserCommentToDB,
    getAllUserComments,
    getUserCommentById,
    replaceUserCommentById,
    updateUserCommentById,
    deleteUserCommentById
)


router = APIRouter(
    prefix="/user-comment",
    tags=["User Comments"]
)


@router.post("/")
def add_UserComment_To_DB(data: UserCommentModel) -> None:
    addUserCommentToDB(data)
    return data
    
    
    
@router.get("/")
def get_All_UserComments():
    return getAllUserComments()

@router.get("/{comment_id}")
def get_UserComment_By_Id(comment_id: UUID4):
    return getUserCommentById(comment_id)


@router.put("/{comment_id}")
def replace_UserComment_By_Id(comment_id: UUID4, data: UserCommentModel):
    return replaceUserCommentById(comment_id, data)


@router.patch("/{comment_id}")
def update_UserComment_By_Id(comment_id: UUID4, field: str, data: str):
    return updateUserCommentById(comment_id, field, data)


@router.delete("/{comment_id}")
def delete_UserComment_By_Id(comment_id: UUID4):
    return deleteUserCommentById(comment_id)