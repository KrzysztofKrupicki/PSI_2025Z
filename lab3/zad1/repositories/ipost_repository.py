from abc import ABC
from typing import Iterable

from zad1.domains.post import PostRecord


class IPostRepository(ABC):
    async def get_all_posts(self) -> Iterable[PostRecord]:
        pass

    async def get_all_posts_json(self) -> list[dict]:
        pass
