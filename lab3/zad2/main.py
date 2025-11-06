import asyncio
import json


from repositories.post_repository import PostRepository
from services.post_service import PostService
from repositories.comment_repository import CommentRepository
from services.comment_service import CommentService


async def main() -> None:
    post_repository = PostRepository()
    post_service = PostService(post_repository)
    comments_repository = CommentRepository()
    comments_service = CommentService(comments_repository)
    all_posts = await post_service.get_all_posts()
    print(f'Posts in cache: {len(post_repository._cached_posts)}')
    post_id_3 = await post_service.get_post_by_id(3)
    print(f'Get post id: {post_id_3.id} Last accessed: {post_id_3.last_accessed}')
    await asyncio.sleep(3)
    post_id_7 = await post_service.get_post_by_id(7)
    print(f'Get post id: {post_id_7.id} Last accessed: {post_id_7.last_accessed}')
    await asyncio.sleep(3)
    await post_service.cleanup_not_used_posts(4)
    print(f'Posts in cache: {len(post_repository._cached_posts)}')
    await asyncio.sleep(2)
    await comments_service.get_comment_by_id(4)
    await asyncio.sleep(3)
    await comments_service.get_comment_by_id(2)
    await asyncio.sleep(4)
    await comments_service.get_comment_by_id(6)
    await asyncio.sleep(2)
    sorted_comments_desc = await comments_service.sort_by_last_usage_time_descending()
    for comment in sorted_comments_desc:
        print(f'Comment id: {comment.id} Last accessed: {comment.last_accessed}')


if __name__ == '__main__':
    asyncio.run(main())
