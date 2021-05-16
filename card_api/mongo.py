"""Module to initialize the Mongo database"""

import mongoengine as _me
import os
from pathlib import Path
import requests

os.sys.path.append("{0}/config".format(Path(os.getcwd()).parent))

import card_api.config.mongo_db as _conf

_me.connect(
    db=_conf.MONGO_DATABASE,
    host=_conf.MONGO_SERVERS,
    port=27016,
    username=_conf.MONGO_USERNAME,
    password=_conf.MONGO_PASSWORD,
    authentication_source="admin",
)
