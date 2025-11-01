import asyncio
import json

from repositories.post_repository import PostRepository
from services.post_service import PostService


async def main() -> None:
    repository = PostRepository()
    service = PostService(repository)
    posts = await service.get_all_posts()
    raw_data = await repository.get_all_posts_json()
    print(json.dumps(raw_data, indent=4))
    for post in posts:
        print(f'Post id: {post.id}\n'
              f'Title: {post.title}\n')
    title_filter = await service.filter_posts_by_title_keyword('nam')
    for post in title_filter:
        print(post)

    body_filter = await service.filter_posts_by_body_keyword('neque minima')
    for post in body_filter:
        print(post)


if __name__ == '__main__':
    asyncio.run(main())
