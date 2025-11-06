from abc import ABC, abstractmethod
from typing import Iterable

from domains.comment import CommentRecord


class ICommentRepository(ABC):
    @abstractmethod
    async def get_all_comments(self) -> Iterable[CommentRecord]:
        pass

    @abstractmethod
    async def get_all_comments_json(self) -> list[dict]:
        pass