"""Module to initialize the Mongo database"""

import os as _os
from pathlib import Path

import mongoengine as _me

_os.sys.path.append("{0}/config".format(Path(_os.getcwd()).parent))

import card_api.config.mongo_db as _conf  # noqa E402

_me.connect(
    db=_conf.MONGO_DATABASE,
    host=_conf.MONGO_SERVERS,
    port=int(_os.getenv("MONGO_DB_PORT")),
    username=_conf.MONGO_USERNAME,
    password=_conf.MONGO_PASSWORD,
    authentication_source="admin",
)
