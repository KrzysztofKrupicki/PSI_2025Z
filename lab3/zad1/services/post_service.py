from typing import Iterable

from zad1.domains.post import PostRecord
from zad1.repositories.ipost_repository import IPostRepository
from zad1.services.ipost_service import IPostService


class PostService(IPostService):
    repository: IPostRepository

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository

    async def get_all_posts(self) -> Iterable[PostRecord]:
        return await self.repository.get_all_posts() or []

    async def filter_posts_by_title_keyword(self, title_keyword: str) -> Iterable[PostRecord]:
        all_posts = await self.get_all_posts()
        return [post for post in all_posts if title_keyword.lower() in post.title.lower()]

    async def filter_posts_by_body_keyword(self, body_keyword: str) -> Iterable[PostRecord]:
        all_posts = await self.get_all_posts()
        return [post for post in all_posts if body_keyword.lower() in post.body.lower()]
