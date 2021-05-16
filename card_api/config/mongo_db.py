"""Config for mongo db"""
import typing as _t
import os as _os

__all__ = (
    "MONGO_DATABASE",
    "MONGO_PASSWORD",
    "MONGO_USERNAME",
)


# MONGO_DATABASE: str = "cardapi"
# MONGO_USERNAME: str = _os.getenv("MONGO_USERNAME")
# MONGO_PASSWORD: str = _os.getenv("MONGO_PASSWORD")
# MONGO_SERVERS: _t.Sequence[str] = ["localhost"]


MONGO_DATABASE: str = "carddb"
MONGO_USERNAME: str = "carduser"
MONGO_PASSWORD: str = "cardpass"
MONGO_SERVERS: _t.Sequence[str] = ["localhost"]
