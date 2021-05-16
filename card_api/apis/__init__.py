import card_api.apis.app as _app

app = _app.create_app()
from card_api.mongo import *
