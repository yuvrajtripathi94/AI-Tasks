import redis

cache = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def get_cache(key):
    return cache.get(key)

def set_cache(key, value):
    cache.setex(key, 3600, value)