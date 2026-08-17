from app.db import UserCommentDB
from app.models.UserCommentModel import UserCommentModel
from pydantic import UUID4
from uuid import UUID


def change_course_id(
    commentid: UUID4,
    course_id: str
) -> UserCommentModel:

    try:
        value: UUID = UUID(course_id)

        if value.version != 4:
            raise ValueError("Not UUID4")

    except (ValueError, AttributeError):
        raise ValueError("course_id must be a valid UUID4.")

    for comment in UserCommentDB:
        if comment.commentid == commentid:
            comment.course_id = value
            return comment

    raise ValueError("Comment not found")


def change_user_id(
    commentid: UUID4,
    user_id: str
) -> UserCommentModel:

    try:
        value: UUID = UUID(user_id)

        if value.version != 4:
            raise ValueError("Not UUID4")

    except (ValueError, AttributeError):
        raise ValueError("user_id must be a valid UUID4.")

    for comment in UserCommentDB:
        if comment.commentid == commentid:
            comment.user_id = value
            return comment

    raise ValueError("Comment not found")


def change_parent_comment(
    commentid: UUID4,
    parent_comment: str
) -> UserCommentModel:

    try:
        value: UUID = UUID(parent_comment)

        if value.version != 4:
            raise ValueError("Not UUID4")

    except (ValueError, AttributeError):
        raise ValueError("parent_comment must be a valid UUID4.")

    for comment in UserCommentDB:
        if comment.commentid == commentid:
            comment.parent_comment = value
            return comment

    raise ValueError("Comment not found")


def change_content(
    commentid: UUID4,
    content: str
) -> UserCommentModel:

    for comment in UserCommentDB:
        if comment.commentid == commentid:
            comment.content = content
            return comment

    raise ValueError("Comment not found")