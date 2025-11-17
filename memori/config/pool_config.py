"""
Database connection pool configuration for Memori.

Provides centralized defaults for SQLAlchemy connection pool settings.
These can be overridden via environment variables or per-instance parameters.
"""

import os


class PoolConfig:
    """
    Centralized database connection pool configuration.
    
    Defaults can be overridden via environment variables:
    - MEMORI_DATABASE__POOL_SIZE
    - MEMORI_DATABASE__POOL_MAX_OVERFLOW
    - MEMORI_DATABASE__POOL_TIMEOUT
    - MEMORI_DATABASE__POOL_RECYCLE
    - MEMORI_DATABASE__POOL_PRE_PING
    """

    def __init__(self) -> None:
        """Initialize pool config with defaults or environment overrides."""
        self.DEFAULT_POOL_SIZE = int(
            os.getenv("MEMORI_DATABASE__POOL_SIZE", "5")
        )
        self.DEFAULT_MAX_OVERFLOW = int(
            os.getenv("MEMORI_DATABASE__POOL_MAX_OVERFLOW", "10")
        )
        self.DEFAULT_POOL_TIMEOUT = int(
            os.getenv("MEMORI_DATABASE__POOL_TIMEOUT", "30")
        )
        self.DEFAULT_POOL_RECYCLE = int(
            os.getenv("MEMORI_DATABASE__POOL_RECYCLE", "1800")
        )
        self.DEFAULT_POOL_PRE_PING = (
            os.getenv("MEMORI_DATABASE__POOL_PRE_PING", "true").lower() == "true"
        )


pool_config = PoolConfig()
