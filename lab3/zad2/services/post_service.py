from datetime import datetime, timedelta
from typing import Iterable

from domains.post import PostRecord
from repositories.ipost_repository import IPostRepository
from services.ipost_service import IPostService


class PostService(IPostService):
    repository: IPostRepository

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository

    async def get_all_posts(self) -> Iterable[PostRecord]:
        return await self.repository.get_all_posts()

    async def get_post_by_id(self, post_id: int) -> PostRecord | None:
        all_posts = await self.repository.get_all_posts()
        for post in all_posts:
            if post.id == post_id:
                post.last_accessed = datetime.now()
                return post
        return None

    async def filter_posts_by_title_keyword(self, title_keyword: str) -> Iterable[PostRecord]:
        all_posts = await self.get_all_posts()
        return [post for post in all_posts if title_keyword.lower() in post.title.lower()]

    async def filter_posts_by_body_keyword(self, body_keyword: str) -> Iterable[PostRecord]:
        all_posts = await self.get_all_posts()
        return [post for post in all_posts if body_keyword.lower() in post.body.lower()]

    async def sort_by_last_usage_time_ascending(self) -> Iterable[PostRecord]:
        return sorted(self.repository._cached_posts, key=lambda p: p.last_accessed)
    
    async def sort_by_last_usage_time_ascending(self) -> Iterable[PostRecord]:
        return sorted(self.repository._cached_posts, key=lambda p: p.last_accessed, reverse=True)

    async def cleanup_not_used_posts(self, seconds: int) -> None:
        time_limit = datetime.now() - timedelta(seconds=seconds)
        before = len(self.repository._cached_posts)
        self.repository._cached_posts = [post for post in self.repository._cached_posts if post.last_accessed > time_limit]
        after = len(self.repository._cached_posts)
        print(f'Deleted {before-after} posts')