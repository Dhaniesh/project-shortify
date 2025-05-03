import os
import redis
from redis.exceptions import RedisError

# Get Redis host and port from environment variables with defaults
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = os.environ.get("REDIS_PORT", 6379)

try:
    # Initialize Redis connection
    r = redis.Redis(host=redis_host,
                    port=int(redis_port),
                    decode_responses=True
                    )
    # Test the connection
    r.ping()
except (RedisError, ValueError) as e:
    # Handle connection errors or invalid port
    raise RuntimeError(f"Failed to connect to Redis: {e}")
