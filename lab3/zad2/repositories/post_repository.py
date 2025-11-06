from datetime import datetime, timedelta

import aiohttp
from typing import Iterable

from domains.post import PostRecord
from repositories.ipost_repository import IPostRepository
from utils import consts


class PostRepository(IPostRepository):
    def __init__(self):
        self._cached_raw: list[dict] = []
        self._cached_posts: list[PostRecord] = []

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_POST_URL) as response:
                if response.status != 200:
                    return None
                return await response.json()

    def _parse_params(self, params: Iterable[dict]) -> Iterable[PostRecord]:
        return [PostRecord(
            user_id=record.get("userId"),
            id=record.get("id"),
            title=record.get("title"),
            body=record.get("body")
        )
            for record in params
        ]

    async def get_all_posts(self) -> Iterable[PostRecord]:
        if not self._cached_posts:
            if not self._cached_raw:
                self._cached_raw = await self._get_params()
            if self._cached_raw:
                self._cached_posts = self._parse_params(self._cached_raw)
        return self._cached_posts

    async def get_all_posts_json(self) -> list[dict]:
        if not self._cached_raw:
            self._cached_raw = await self._get_params()
        return self._cached_raw
