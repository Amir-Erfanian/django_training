import redis
from django.conf import settings
# utils/cache_utils.py
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

def invalidate_book_caches(book_id=None):
    """Invalidate all book-related caches"""
    cache.delete('book_list_all')
    cache.delete('home_stats')
    if book_id:
        cache.delete(f'book_detail_{book_id}')
        cache.delete(f'book_related_{book_id}')
    # More aggressive: delete all pattern matches
    cache.delete_pattern('book_*')
    logger.info(f"Book caches invalidated for book {book_id if book_id else 'all'}")

def get_cached_book_list():
    """Get cached book list with fallback"""
    cache_key = 'book_list_all'
    books = cache.get(cache_key)
    if books is None:
        from .models import Book
        books = Book.objects.select_related('author').prefetch_related('categories')
        cache.set(cache_key, books, timeout=300)
    return books

def cache_book_detail(book_id, book_instance=None):
    """Cache a book detail with fallback"""
    cache_key = f'book_detail_{book_id}'
    if book_instance is None:
        from .models import Book
        book_instance = Book.objects.get(id=book_id)
    cache.set(cache_key, book_instance, timeout=900)
    return book_instance

class RedisClient:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                decode_responses=True,
                socket_connect_timeout=5,
                socket_timeout=5,
                retry_on_timeout=True
            )
        return cls._instance
    
    def get_client(self):
        return self.client

# Singleton instance
redis_client = RedisClient().get_client()