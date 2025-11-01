from typing import Iterable
from abc import ABC

from zad1.domains.post import PostRecord


class IPostService(ABC):
    async def get_all_posts(self) -> Iterable[PostRecord]:
        pass

    async def filter_posts_by_title_keyword(self, title_keyword: str) -> Iterable[PostRecord]:
        pass

    async def filter_posts_by_body_keyword(self, body_keyword: str) -> Iterable[PostRecord]:
        pass
