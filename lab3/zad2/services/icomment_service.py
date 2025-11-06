from typing import Iterable
from abc import ABC, abstractmethod

from domains.comment import CommentRecord


class ICommentService(ABC):
    @abstractmethod
    async def get_all_comments(self) -> Iterable[CommentRecord]:
        pass

    @abstractmethod
    async def get_comment_by_id(self, comment_id: int) -> CommentRecord | None:
        pass

    @abstractmethod
    async def filter_comments_by_author_keyword(self, author_keyword: str) -> Iterable[CommentRecord]:
        pass
    
    @abstractmethod
    async def filter_comments_by_body_keyword(self, body_keyword: str) -> Iterable[CommentRecord]:
        pass

    @abstractmethod
    async def cleanup_not_used_comments(self, seconds: int) -> None:
        pass
