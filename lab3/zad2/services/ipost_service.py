from typing import Iterable
from abc import ABC, abstractmethod

from domains.post import PostRecord


class IPostService(ABC):
    @abstractmethod
    async def get_all_posts(self) -> Iterable[PostRecord]:
        pass

    @abstractmethod
    async def get_post_by_id(self, post_id: int) -> PostRecord:
        pass

    @abstractmethod
    async def filter_posts_by_title_keyword(self, title_keyword: str) -> Iterable[PostRecord]:
        pass

    @abstractmethod
    async def filter_posts_by_body_keyword(self, body_keyword: str) -> Iterable[PostRecord]:
        pass

    @abstractmethod
    async def cleanup_not_used_posts(self, seconds: int) -> None:
        pass