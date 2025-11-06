from datetime import datetime, timedelta
from typing import Iterable

from domains.comment import CommentRecord
from repositories.icomment_repository import ICommentRepository
from services.icomment_service import ICommentService


class CommentService(ICommentService):
    repository: ICommentRepository

    def __init__(self, repository: ICommentRepository) -> None:
        self.repository = repository

    async def get_all_comments(self) -> Iterable[CommentRecord]:
        return await self.repository.get_all_comments()

    async def get_comment_by_id(self, comment_id: int) -> CommentRecord | None:
        all_comments = await self.repository.get_all_comments()
        for comment in all_comments:
            if comment.id == comment_id:
                comment.last_accessed = datetime.now()
                return comment
        return None

    async def filter_comments_by_author_keyword(self, author_keyword: str) -> Iterable[CommentRecord]:
        all_comments = await self.get_all_comments()
        return [comment for comment in all_comments if author_keyword.lower() in comment.email.lower()]

    async def filter_comments_by_body_keyword(self, body_keyword: str) -> Iterable[CommentRecord]:
        all_comments = await self.get_all_comments()
        return [comment for comment in all_comments if body_keyword.lower() in comment.body.lower()]

    async def sort_by_last_usage_time_ascending(self) -> Iterable[CommentRecord]:
        return sorted(self.repository._cached_comments, key=lambda c: c.last_accessed)
    
    async def sort_by_last_usage_time_descending(self) -> Iterable[CommentRecord]:
        return sorted(self.repository._cached_comments, key=lambda c: c.last_accessed, reverse=True)
    
    async def cleanup_not_used_comments(self, seconds: int) -> None:
        time_limit = datetime.now() - timedelta(seconds=seconds)
        before = len(self.repository._cached_comments)
        self.repository._cached_comments = [comment for comment in self.repository._cached_comments if comment.last_accessed > time_limit]
        after = len(self.repository._cached_comments)
        print(f'Deleted {before-after} comments')
