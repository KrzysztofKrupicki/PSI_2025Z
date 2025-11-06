from abc import ABC, abstractmethod
from typing import Iterable

from domains.post import PostRecord


class IPostRepository(ABC):
    @abstractmethod
    async def get_all_posts(self) -> Iterable[PostRecord]:
        pass

    @abstractmethod
    async def get_all_posts_json(self) -> list[dict]:
        pass