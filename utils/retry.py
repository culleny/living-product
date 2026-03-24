import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def retry_once(func):
    """Retry decorator that attempts once on timeout/connection errors."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "timeout" in str(e).lower() or "connection" in str(e).lower():
                logger.warning(f"Retrying {func.__name__} after error: {e}")
                time.sleep(2)
                return func(*args, **kwargs)
            raise
    return wrapper
