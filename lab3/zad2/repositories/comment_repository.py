from datetime import datetime, timedelta

import aiohttp
from typing import Iterable

from domains.comment import CommentRecord
from repositories.icomment_repository import ICommentRepository
from utils import consts


class CommentRepository(ICommentRepository):
    def __init__(self):
        self._cached_raw: list[dict] = []
        self._cached_comments: list[CommentRecord] = []

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_COMMENT_URL) as response:
                if response.status != 200:
                    return None
                return await response.json()

    def _parse_params(self, params: Iterable[dict]) -> Iterable[CommentRecord]:
        return [CommentRecord(
            post_id=record.get("postId"),
            id=record.get("id"),
            name=record.get("name"),
            email=record.get("email"),
            body=record.get("body")
        )
            for record in params
        ]

    async def get_all_comments(self) -> Iterable[CommentRecord]:
        if not self._cached_comments:
            if not self._cached_raw:
                self._cached_raw = await self._get_params()
            if self._cached_raw:
                self._cached_comments = self._parse_params(self._cached_raw)
        return self._cached_comments

    async def get_all_comments_json(self) -> list[dict]:
        if not self._cached_raw:
            self._cached_raw = await self._get_params()
        return self._cached_raw
